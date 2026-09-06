from django.core.management.base import BaseCommand

from resume.resume_data import RESUME_DATA
from resume.models import (
    PersonalInfo,
    ExpertiseItem,
    ExperienceItem,
    EducationItem,
    SkillItem,
    LanguageItem,
)


class Command(BaseCommand):
    help = "Load/refresh resume content in the database from resume/resume_data.py"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Delete existing resume content first and reload from resume_data.py",
        )

    def handle(self, *args, **options):
        if PersonalInfo.objects.exists() and not options["force"]:
            self.stdout.write(self.style.WARNING(
                "Resume data already exists in the database. "
                "Run with --force to wipe and reload from resume_data.py."
            ))
            return

        if options["force"]:
            PersonalInfo.objects.all().delete()
            ExpertiseItem.objects.all().delete()
            ExperienceItem.objects.all().delete()
            EducationItem.objects.all().delete()
            SkillItem.objects.all().delete()
            LanguageItem.objects.all().delete()

        contacts = RESUME_DATA.get("contacts", {})
        contact_block = RESUME_DATA.get("contact_block", {})

        PersonalInfo.objects.create(
            name=RESUME_DATA.get("name", ""),
            title=RESUME_DATA.get("title", ""),
            about_heading=RESUME_DATA.get("about_heading", ""),
            about_text=RESUME_DATA.get("about_text", ""),
            email=contacts.get("email", ""),
            phone=contacts.get("phone", ""),
            linkedin_url=contacts.get("linkedin_url", ""),
            linkedin_label=contacts.get("linkedin_label", ""),
            github_url=contacts.get("github_url", ""),
            github_label=contacts.get("github_label", ""),
            contact_phone=contact_block.get("phone", ""),
            contact_email=contact_block.get("email", ""),
            contact_email2=contact_block.get("email2", ""),
        )

        for i, item in enumerate(RESUME_DATA.get("expertise", [])):
            ExpertiseItem.objects.create(order=i, **item)

        for i, item in enumerate(RESUME_DATA.get("experience", [])):
            ExperienceItem.objects.create(order=i, **item)

        for i, item in enumerate(RESUME_DATA.get("education", [])):
            EducationItem.objects.create(order=i, **item)

        for i, item in enumerate(RESUME_DATA.get("skills", [])):
            SkillItem.objects.create(order=i, **item)

        for i, item in enumerate(RESUME_DATA.get("languages", [])):
            LanguageItem.objects.create(order=i, **item)

        self.stdout.write(self.style.SUCCESS("Resume data loaded into the database successfully."))
