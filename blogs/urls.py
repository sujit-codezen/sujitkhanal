from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path('list/',views.blog_list, name="blog_list"),
    path('<str:slug>/',views.BlogDetailView.as_view(), name="blog_detail"),
]