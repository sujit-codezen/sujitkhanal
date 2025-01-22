from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length = 50, null=True)
    phone_number = models.CharField(max_length = 20, null=True)
    email = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200, null=True)
    message = models.CharField(max_length= 200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    class Meta:
        ordering = ['-date']