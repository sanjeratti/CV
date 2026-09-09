import os

from django.conf import settings
from django.core.management.base import BaseCommand

from resume.views import get_resume_context

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
    from reportlab.lib.enums import TA_LEFT
except ImportError:
    raise SystemExit(
        "reportlab is not installed. Run: pip install reportlab"
    )

# Where the file ends up. Must match the {% static %} path used in index.html.
OUTPUT_RELATIVE_PATH = os.path.join("files", "Sanzhar_Abdykerimov_CV.pdf")


def esc(text):
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Command(BaseCommand):
    help = "Generate/refresh the downloadable CV PDF (static/files/...) from the current resume data."

    def handle(self, *args, **options):
        resume = get_resume_context()

        # Figure out where the project's static source folder is.
        static_dirs = getattr(settings, "STATICFILES_DIRS", None)
        if static_dirs:
            static_root = static_dirs[0]
        else:
            static_root = os.path.join(settings.BASE_DIR, "static")

        output_path = os.path.join(static_root, OUTPUT_RELATIVE_PATH)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        styles = getSampleStyleSheet()
        name_style = ParagraphStyle("NameStyle", parent=styles["Title"], fontSize=22, leading=26,
                                     textColor=colors.HexColor("#222222"), spaceAfter=2)
        title_style = ParagraphStyle("TitleStyle", parent=styles["Normal"], fontSize=12,
                                      textColor=colors.HexColor("#e63946"), spaceAfter=10)
        section_style = ParagraphStyle("SectionStyle", parent=styles["Heading2"], fontSize=13,
                                        textColor=colors.HexColor("#e63946"), spaceBefore=14, spaceAfter=6)
        body_style = ParagraphStyle("BodyStyle", parent=styles["Normal"], fontSize=9.5, leading=13,
                                     alignment=TA_LEFT)
        role_style = ParagraphStyle("RoleStyle", parent=styles["Normal"], fontSize=10, leading=13,
                                     textColor=colors.HexColor("#333333"), spaceBefore=6)
        period_style = ParagraphStyle("PeriodStyle", parent=styles["Normal"], fontSize=9, leading=12,
                                       textColor=colors.HexColor("#888888"))
        contact_style = ParagraphStyle("ContactStyle", parent=styles["Normal"], fontSize=9.5, leading=13)

        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=16 * mm,
            bottomMargin=16 * mm,
            title=f"{resume['name']} - CV",
        )

        story = []
        story.append(Paragraph(esc(resume["name"]), name_style))
        story.append(Paragraph(esc(resume["title"]), title_style))

        contacts = resume["contacts"]
        contact_line = (
            f"Email: {esc(contacts['email'])} &nbsp;|&nbsp; Phone: {esc(contacts['phone'])} &nbsp;|&nbsp; "
            f"LinkedIn: {esc(contacts['linkedin_label'])} &nbsp;|&nbsp; GitHub: {esc(contacts['github_label'])}"
        )
        story.append(Paragraph(contact_line, contact_style))
        story.append(Spacer(1, 8))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#dddddd")))

        story.append(Paragraph("ABOUT ME", section_style))
        story.append(Paragraph(esc(resume["about_text"]), body_style))

        story.append(Paragraph("EXPERTISE", section_style))
        for item in resume["expertise"]:
            story.append(Paragraph(f"<b>{esc(item['title'])}</b> — {esc(item['subtitle'])}", body_style))
            story.append(Spacer(1, 2))

        story.append(Paragraph("WORK EXPERIENCE", section_style))
        for job in resume["experience"]:
            story.append(Paragraph(esc(job["period"]), period_style))
            story.append(Paragraph(f"<b>{esc(job['role'])}</b>", role_style))
            desc_html = esc(job["description"]).replace("\n", "<br/>")
            story.append(Paragraph(desc_html, body_style))
            story.append(Spacer(1, 6))

        story.append(Paragraph("EDUCATION", section_style))
        for edu in resume["education"]:
            story.append(Paragraph(f"<font color='#888888'>{esc(edu['period'])}</font> — {esc(edu['title'])}", body_style))
            story.append(Spacer(1, 2))

        story.append(Paragraph("SKILLS", section_style))
        skills_text = ", ".join(esc(s["label"]) for s in resume["skills"])
        story.append(Paragraph(skills_text, body_style))

        story.append(Paragraph("LANGUAGES", section_style))
        langs_text = ", ".join(f"{esc(l['label'])} ({l['percent']}%)" for l in resume["languages"])
        story.append(Paragraph(langs_text, body_style))

        doc.build(story)

        self.stdout.write(self.style.SUCCESS(f"CV PDF generated: {output_path}"))
