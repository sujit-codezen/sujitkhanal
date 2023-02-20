from django.db import models
from taggit.managers import TaggableManager
from core.utils import TimeStampedModel

# Create your models here.
class Project(TimeStampedModel):
    PROJECT_TYPE_CHOICES = (
        ("Android App", "Android App"),
        ("Desktop App", "Desktop App"),
        ("Web App", "Web App"),
        ("IOS App", "IOS App"),
        ("Terminal Code", "Terminal Code"),
    )
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=100)
    project_type = models.CharField(
        max_length = 20,
        choices = PROJECT_TYPE_CHOICES,
        default = 'Web App'
    )
    language_used = TaggableManager()
    image = models.ImageField(default="projects/image/default.jpg", upload_to="projects/image")
    project_url = models.CharField(max_length=255, blank=True, null=True)
    github_url = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)


# class ProjectImage(TimeStampedModel):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_image')
#     image = models.ImageField(upload_to='projects/image')
