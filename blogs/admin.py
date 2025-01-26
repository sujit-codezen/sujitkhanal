from django.contrib import admin
from .models import Post, Category, Tag, Comment, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title
    inlines = [PostImageInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
