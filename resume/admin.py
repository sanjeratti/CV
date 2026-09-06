from django.contrib import admin
from .models import (
    ContactMessage,
    PersonalInfo,
    ExpertiseItem,
    ExperienceItem,
    EducationItem,
    SkillItem,
    LanguageItem,
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')


@admin.register(ExpertiseItem)
class ExpertiseItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order')
    list_editable = ('order',)


@admin.register(ExperienceItem)
class ExperienceItemAdmin(admin.ModelAdmin):
    list_display = ('period', 'role', 'order')
    list_editable = ('order',)


@admin.register(EducationItem)
class EducationItemAdmin(admin.ModelAdmin):
    list_display = ('period', 'title', 'order')
    list_editable = ('order',)


@admin.register(SkillItem)
class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'percent', 'order')
    list_editable = ('percent', 'order')


@admin.register(LanguageItem)
class LanguageItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'percent', 'order')
    list_editable = ('percent', 'order')

