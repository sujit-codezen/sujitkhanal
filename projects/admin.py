from django.contrib import admin

from .models import Project, ProjectImage, ProgrammingLanguage

admin.site.register(ProgrammingLanguage)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fields = (
            'image',
        )
    can_delete = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type', 'project_url', 'github_url', 'video_url')
    list_filter = ('project_name', 'project_type',)
    search_fields = ('project_name',)
    exclude = ('created','modified',)

    
    inlines = [ProjectImageInline]