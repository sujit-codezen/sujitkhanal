# Generated by Django 5.0.7 on 2025-01-21 16:05

import ckeditor_uploader.fields
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_mydetail_address_mydetail_coding_started_at_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mydetail',
            options={'verbose_name': 'My Details', 'verbose_name_plural': 'My Details'},
        ),
        migrations.AddField(
            model_name='mydetail',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='About'),
        ),
        migrations.AddField(
            model_name='mydetail',
            name='about_short',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mydetail',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mydetail',
            name='specialized_at',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
