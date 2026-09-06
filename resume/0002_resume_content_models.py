from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your Name', max_length=255)),
                ('title', models.CharField(default='Your Job Title', max_length=255)),
                ('about_heading', models.CharField(blank=True, max_length=255)),
                ('about_text', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('linkedin_url', models.URLField(blank=True)),
                ('linkedin_label', models.CharField(blank=True, max_length=255)),
                ('github_url', models.URLField(blank=True)),
                ('github_label', models.CharField(blank=True, max_length=255)),
                ('contact_phone', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('contact_email2', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'Personal info',
                'verbose_name_plural': 'Personal info',
            },
        ),
        migrations.CreateModel(
            name='ExpertiseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(help_text='Themify icon class, e.g. ti-widget', max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=500)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ExperienceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='EducationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SkillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=500)),
                ('percent', models.PositiveIntegerField(default=50)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='LanguageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('percent', models.PositiveIntegerField(default=50)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
    ]
