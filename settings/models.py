from django.db import models
from core.utils import TimeStampedModel
from core.utils import SingletonModel
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from projects.models import Project

# Create your models here.
class Assignment(SingletonModel):
    default_price = models.IntegerField(default=80)
    urgent_price = models.IntegerField(default=40)
    medium_price = models.IntegerField(default=20)
    description = RichTextUploadingField(default="Description")

class MyDetail(SingletonModel):
    full_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, null=True)
    logo = models.FileField(default="image/default.jpg", upload_to="image")
    dob = models.DateField(null=True)
    contact_number = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    country_code = models.CharField(max_length=10,null=True)
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=255,null=True)
    youtube_channel = models.CharField(max_length=255)
    github_url = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=100, null=True)
    instagram_url = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(default="+9779842765535", max_length=100)
    mail = models.CharField(max_length=255)
    website = models.CharField(max_length=100)
    display_photo = models.ImageField(default="image/default.jpg", upload_to="image")
    second_display_photo = models.ImageField(default="image/default.jpg", upload_to="image")
    cv = models.FileField(default="cv/default.pdf", upload_to="cv")
    coding_started_at = models.DateField(null=True)
    profession = models.CharField(max_length=100,null=True)
    specialized_at = TaggableManager()
    about = RichTextUploadingField(default="About")
    about_short = models.CharField(max_length=255, null=True)
    slogon = RichTextUploadingField(default="Slogon")
    google_map_url = models.CharField(max_length=1000, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    
    
    
    class Meta:
        verbose_name = "My Details"
        verbose_name_plural = "My Details"
        
    
    def __str__(self):
        return self.full_name
    
    def get_age(self):
        import datetime
        return (datetime.datetime.now().year - self.dob.year) - 1
    
    def get_coding_started_at(self):
        import datetime
        return datetime.datetime.now().year - self.coding_started_at.year
    
    def get_completed_projects(self):
        return Project.objects.filter(is_completed=True).count()
    
    
class Knowledge(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField(default="Description")
    
    class Meta:
        verbose_name = "Knowledge"
        verbose_name_plural = "Knowledges"
        
    def __str__(self):
        return self.title
    
class Education(TimeStampedModel):
    school_name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    gpa = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_present_here = models.BooleanField(default=False)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
        
    def __str__(self):
        return self.school_name
    
class Experience(TimeStampedModel):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_present_here = models.BooleanField(default=False)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        
    def __str__(self):
        return self.company_name
    
class Skill(TimeStampedModel):
    skill_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    percentage = models.IntegerField()
    logo = models.ImageField(default="image/default.jpg", upload_to="image")
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        
    def __str__(self):
        return self.skill_name