from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .resume_data import RESUME_DATA
from .models import (
    PersonalInfo,
    ExpertiseItem,
    ExperienceItem,
    EducationItem,
    SkillItem,
    LanguageItem,
)


def get_resume_context():
    """Build the same 'resume' dict shape the template expects, but sourced
    from the database (editable in /admin) instead of the static file."""
    personal = PersonalInfo.objects.first()
    if personal is None:
        # DB not seeded yet (e.g. migrations not run) — fall back to the file.
        return RESUME_DATA

    return {
        "name": personal.name,
        "title": personal.title,
        "about_heading": personal.about_heading,
        "about_text": personal.about_text,
        "contacts": {
            "email": personal.email,
            "phone": personal.phone,
            "linkedin_url": personal.linkedin_url,
            "linkedin_label": personal.linkedin_label,
            "github_url": personal.github_url,
            "github_label": personal.github_label,
        },
        "expertise": list(ExpertiseItem.objects.values("icon", "title", "subtitle")),
        "experience": list(ExperienceItem.objects.values("period", "role", "description")),
        "education": list(EducationItem.objects.values("period", "title")),
        "skills": list(SkillItem.objects.values("label", "percent")),
        "languages": list(LanguageItem.objects.values("label", "percent")),
        "contact_block": {
            "phone": personal.contact_phone,
            "email": personal.contact_email,
            "email2": personal.contact_email2,
        },
    }


def index(request):
    return render(request, 'index.html', {'resume': get_resume_context()})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form, 'resume': get_resume_context()})

