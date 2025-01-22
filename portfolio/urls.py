from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download-cv/', views.download_cv, name='download_cv'),
]