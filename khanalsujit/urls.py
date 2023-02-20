from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

url_patterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('project/', include('projects.urls')),
    path('contact', include('contact.urls')),
]

urlpatterns = static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + url_patterns