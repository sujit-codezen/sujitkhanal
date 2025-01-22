from django.db import models
from taggit.managers import TaggableManager
from core.utils import TimeStampedModel
from ckeditor.fields import RichTextField
from django.utils.text import slugify

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
    project_description = RichTextField()
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
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.project_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.project_name}-{self.id}")
        super(Project, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f"/project/{self.slug}/"


# class ProjectImage(TimeStampedModel):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_image')
#     image = models.ImageField(upload_to='projects/image')
