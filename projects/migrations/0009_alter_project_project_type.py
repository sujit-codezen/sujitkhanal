# Generated by Django 5.0.7 on 2025-01-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_remove_project_language_used_project_language_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Android App', 'Android App'), ('Desktop App', 'Desktop App'), ('Web App', 'Web App'), ('IOS App', 'IOS App'), ('Terminal Code', 'Terminal Code'), ('Script', 'Script'), ('API', 'API')], default='Web App', max_length=20),
        ),
    ]
