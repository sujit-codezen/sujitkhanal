# Generated by Django 5.0.7 on 2025-01-21 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_mydetail_slogon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mydetail',
            name='nick_name',
        ),
    ]
