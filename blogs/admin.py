from django.contrib import admin
from .models import Post, Category, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
