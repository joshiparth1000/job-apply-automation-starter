from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "resumes" / "tailored_resume.pdf"


def build_resume() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=20,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=12,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=13,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Role",
            parent=styles["Body"],
            fontName="Helvetica-Bold",
            spaceAfter=2,
        )
    )

    story = []
    story.append(Paragraph("Candidate Name", styles["Name"]))
    story.append(
        Paragraph(
            "City, ST | 555-555-5555 | you@example.com | linkedin.com/in/example",
            styles["Meta"],
        )
    )

    story.append(Paragraph("Professional Summary", styles["Section"]))
    story.append(
        Paragraph(
            "Senior platform and infrastructure engineering leader with experience in cloud platforms, reliability engineering, automation, observability, and developer enablement.",
            styles["Body"],
        )
    )

    story.append(Paragraph("Core Skills", styles["Section"]))
    story.append(
        Paragraph(
            "AWS; Kubernetes; Terraform; CI/CD; Observability; Platform Engineering; SRE; DevOps; Infrastructure Automation",
            styles["Body"],
        )
    )

    story.append(Paragraph("Experience", styles["Section"]))
    experience = [
        (
            "Principal Platform Engineer | Example Company | 2022-Present",
            [
                "Led platform engineering initiatives across cloud infrastructure and delivery systems.",
                "Improved reliability, automation, and developer workflows for internal engineering teams.",
            ],
        ),
        (
            "Senior DevOps Engineer | Example Company | 2019-2022",
            [
                "Built CI/CD pipelines and infrastructure automation for cloud-native systems.",
                "Supported observability and operational excellence programs across multiple environments.",
            ],
        ),
    ]

    for role, bullets in experience:
        story.append(Paragraph(role, styles["Role"]))
        story.append(
            ListFlowable(
                [ListItem(Paragraph(item, styles["Body"])) for item in bullets],
                bulletType="bullet",
                leftIndent=16,
            )
        )
        story.append(Spacer(1, 4))

    story.append(Paragraph("Education", styles["Section"]))
    story.append(Paragraph("B.S. in Computer Science | Example University", styles["Body"]))

    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build_resume()
