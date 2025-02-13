# Generated by Django 5.0.7 on 2025-01-24 15:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_short_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='projects/image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_image', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
