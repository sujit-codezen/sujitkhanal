from django.contrib import admin

from .models import Project

# class ProjectImageInline(admin.TabularInline):
#     model = ProjectImage
#     fields = (
#             'image',
#         )
#     can_delete = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type', 'language_used', 'project_url', 'github_url', 'video_url')
    list_filter = ('project_name', 'project_type', 'language_used',)
    search_fields = ('project_name','language_used')
    exclude = ('created','modified',)

    
    # inlines = [ProjectImageInline]