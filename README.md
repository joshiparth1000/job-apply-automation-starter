# Job Apply Automation Starter

A public-safe starter kit for browser-assisted job discovery and application workflows using Playwright, resume tailoring, and local tracking.

This repo is designed to be published safely. It includes only templates and examples, not a real candidate profile.

Job Apply Automation Starter is a public-safe starter kit for building browser-assisted job search and application workflows. It includes sanitized templates for candidate data, application tracking, resume PDF generation, and Playwright-based form automation, while deliberately excluding any personal identity data, browser sessions, screenshots, or live application history.

## Safe By Default

This template intentionally excludes:

- personal identity data
- browser profiles, cookies, and saved sessions
- screenshots and verification artifacts
- real resumes and tailored application files
- application history
- live thread ids and account-specific automation state
- passwords, secrets, and email codes

## Included Files

- `scripts/apply_greenhouse_template.js`
  A minimal Playwright example for Greenhouse-style applications.
- `scripts/build_resume_pdf_template.py`
  A basic PDF resume generator template using ReportLab.
- `candidate.template.json`
  A placeholder local candidate profile.
- `job-application-tracker.template.json`
  A starter tracker to avoid duplicate applications.
- `automation.template.toml`
  A sanitized recurring-job prompt template.

## Recommended Repo Layout

Keep this repository public if you want, but keep the live working files private on your machine.

Public repo:

- scripts
- template JSON files
- docs
- sanitized automation prompt

Private local-only files:

- `candidate.local.json`
- `job-application-tracker.json`
- `resumes/`
- `chrome-automation-profile/`
- screenshots, logs, and submission artifacts

## Quick Start

1. Install Node.js and Python.
2. Install project dependencies:

```powershell
npm install
pip install reportlab
```

3. Create local private working files:

```powershell
Copy-Item candidate.template.json candidate.local.json
Copy-Item job-application-tracker.template.json job-application-tracker.json
New-Item -ItemType Directory resumes -Force
```

4. Add your real candidate data to `candidate.local.json`.
5. Put your resume in the local `resumes/` folder.
6. Update the target job URL and any field mappings in `scripts/apply_greenhouse_template.js`.
7. Run the sample script:

```powershell
npm run apply:greenhouse
```

## Using With Codex

This starter also works well as a Codex-assisted workflow.

Typical setup:

1. Open the repository in Codex.
2. Keep this public repo as the sanitized project structure.
3. Create local-only private files that stay untracked:
   - `candidate.local.json`
   - `job-application-tracker.json`
   - `resumes/`
   - `chrome-automation-profile/`
4. Ask Codex to:
   - tailor a resume for a specific posting
   - update form field mappings for a target careers page
   - run the Playwright script
   - track submitted jobs and blocked applications
   - maintain a recurring automation prompt

Example Codex tasks:

- `Tailor the resume in resumes/base_resume.pdf for this job description and save a new PDF in resumes/.`
- `Update scripts/apply_greenhouse_template.js for this Greenhouse application URL and use candidate.local.json for the inputs.`
- `Run the apply script and tell me if the form was submitted or if a manual step is needed.`
- `Create a recurring Codex automation that searches for roles matching my profile and updates job-application-tracker.json.`

Recommended Codex workflow:

- keep reusable logic in the public repo
- keep personal files and browser state only on your local machine
- let Codex edit the scripts and templates, but do not commit private candidate data back into the repo

If you use Codex desktop automations, store only sanitized prompt templates in git and keep live thread-specific automation state out of the public repository.

## Publishing Advice

Before pushing to GitHub:

- review `git status`
- confirm no private local files are staged
- verify your browser profile and resumes are ignored
- avoid committing screenshots or application confirmations

## Important Limits

- Employer portals vary a lot, so field mappings are not portable.
- Many sites still require manual steps for captcha, SSO, email verification, or anti-bot checks.
- Resume tailoring should stay in a normal recruiter-facing format, not a meta format built around the automation.

## Good Next Steps

If you want to grow this into a stronger open-source project, the next useful additions would be:

- a small config loader for per-site field mappings
- support for Lever, Ashby, and Workday templates
- a tracker CLI
- tests around candidate-data loading and redaction safety
