from django.db import migrations

from resume.resume_data import RESUME_DATA


def seed_data(apps, schema_editor):
    PersonalInfo = apps.get_model('resume', 'PersonalInfo')
    ExpertiseItem = apps.get_model('resume', 'ExpertiseItem')
    ExperienceItem = apps.get_model('resume', 'ExperienceItem')
    EducationItem = apps.get_model('resume', 'EducationItem')
    SkillItem = apps.get_model('resume', 'SkillItem')
    LanguageItem = apps.get_model('resume', 'LanguageItem')

    if PersonalInfo.objects.exists():
        return  # already seeded, don't duplicate

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


def unseed_data(apps, schema_editor):
    for model_name in ("PersonalInfo", "ExpertiseItem", "ExperienceItem", "EducationItem", "SkillItem", "LanguageItem"):
        apps.get_model('resume', model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resume_content_models'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
