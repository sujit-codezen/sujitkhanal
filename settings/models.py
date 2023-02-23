from django.db import models
from core.utils import TimeStampedModel
from core.utils import SingletonModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Assignment(SingletonModel):
    default_price = models.IntegerField(default=80)
    urgent_price = models.IntegerField(default=40)
    medium_price = models.IntegerField(default=20)
    description = RichTextUploadingField(default="Description")

class MyDetail(SingletonModel):
    full_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    youtube_channel = models.CharField(max_length=255)
    github_url = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)
    whatsapp = models.CharField(default="+9779842765535", max_length=100)
    mail = models.CharField(max_length=255)
    website = models.CharField(max_length=100)