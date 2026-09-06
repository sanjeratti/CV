from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name}'


class PersonalInfo(models.Model):
    """Singleton-style model: only one row is expected to exist."""
    name = models.CharField(max_length=255, default="Your Name")
    title = models.CharField(max_length=255, default="Your Job Title")

    about_heading = models.CharField(max_length=255, blank=True)
    about_text = models.TextField(blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)
    linkedin_label = models.CharField(max_length=255, blank=True)
    github_url = models.URLField(blank=True)
    github_label = models.CharField(max_length=255, blank=True)

    contact_phone = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_email2 = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Personal info"
        verbose_name_plural = "Personal info"

    def __str__(self):
        return self.name


class ExpertiseItem(models.Model):
    icon = models.CharField(max_length=100, help_text="Themify icon class, e.g. ti-widget")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class ExperienceItem(models.Model):
    period = models.CharField(max_length=100)
    role = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.period} — {self.role}"


class EducationItem(models.Model):
    period = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.period} — {self.title}"


class SkillItem(models.Model):
    label = models.CharField(max_length=500)
    percent = models.PositiveIntegerField(default=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.label


class LanguageItem(models.Model):
    label = models.CharField(max_length=255)
    percent = models.PositiveIntegerField(default=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.label

