from django.contrib import admin

from .models import MyDetail, Assignment, Knowledge, Education, Experience, Skill
# Register your models here.

admin.site.register(MyDetail)
admin.site.register(Assignment)
admin.site.register(Knowledge)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)