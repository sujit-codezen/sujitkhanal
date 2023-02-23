from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from core.utils import TimeStampedModel
from django.utils import timezone
from taggit.managers import TaggableManager



# Create your models here.

class Assignment(TimeStampedModel):
    ASSIGNMENT_PRIORITY_CHOICES = (
        ("Urgent", "Urgent"),
        ("Medium", "Medium"),
        ("With In 15 Days", "With In 15 Days"),
        ("With In 1 month", "With In 1 month"),
    )
    ASSIGNMENT_STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Working On", "Working On"),
        ("Delivered", "Delivered"),
    )
    assignment_title = models.CharField(max_length=100)
    assignment_description = RichTextUploadingField()
    assignment_priority = models.CharField(choices=ASSIGNMENT_PRIORITY_CHOICES, max_length=100)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    file = models.FileField()
    assignment_status = models.CharField(default='Pending', choices=ASSIGNMENT_STATUS_CHOICES, max_length=100)
    price = models.IntegerField(default=80)
    language_used = TaggableManager()
    date_up_to = models.DateTimeField(default=timezone.now())

    # def save(self, *args, **kwargs):
    #     super(Assignment, self).save(*args, **kwargs)

