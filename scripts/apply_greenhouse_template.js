const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..");
const CANDIDATE_PATH = path.join(ROOT, "candidate.local.json");
const RESUME_PATH = path.join(ROOT, "resumes", "tailored_resume.pdf");
const USER_DATA_DIR = path.join(ROOT, "chrome-automation-profile");
const JOB_URL = "https://job-boards.greenhouse.io/example-company/jobs/1234567";

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

async function fillInput(page, selector, value) {
  const input = page.locator(selector).first();
  await input.waitFor({ state: "visible", timeout: 30000 });
  await input.fill(value);
}

async function setComboboxValue(page, inputId, value) {
  const input = page.locator(`#${inputId}`).first();
  await input.scrollIntoViewIfNeeded();
  await input.click();
  await input.fill(value);
  await page.waitForTimeout(1000);
  const option = page.locator('[role="option"]').filter({ hasText: new RegExp(escapeRegex(value), "i") }).first();
  if (await option.count()) {
    await option.click();
    return;
  }
  await page.keyboard.press("ArrowDown").catch(() => {});
  await page.keyboard.press("Enter").catch(() => {});
}

function escapeRegex(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

async function main() {
  if (!fs.existsSync(CANDIDATE_PATH)) {
    throw new Error("Missing candidate.local.json. Copy candidate.template.json first.");
  }

  const candidate = readJson(CANDIDATE_PATH);

  const context = await chromium.launchPersistentContext(USER_DATA_DIR, {
    headless: false,
    viewport: { width: 1440, height: 960 }
  });

  const page = context.pages()[0] || await context.newPage();
  await page.goto(JOB_URL, { waitUntil: "domcontentloaded", timeout: 60000 });
  await page.waitForLoadState("networkidle", { timeout: 60000 }).catch(() => {});

  await fillInput(page, "#first_name", candidate.firstName);
  await fillInput(page, "#last_name", candidate.lastName);
  await fillInput(page, "#email", candidate.email);
  await setComboboxValue(page, "country", candidate.country);
  await fillInput(page, "#phone", candidate.phone);

  if (fs.existsSync(RESUME_PATH)) {
    await page.locator("#resume").setInputFiles(RESUME_PATH);
  }

  if (candidate.linkedin) {
    const linkedinField = page.locator('input[type="url"], input[name*="linkedin" i]').first();
    if (await linkedinField.count()) {
      await linkedinField.fill(candidate.linkedin);
    }
  }

  console.log(JSON.stringify({
    finalUrl: page.url(),
    title: await page.title()
  }, null, 2));

  await context.close();
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
