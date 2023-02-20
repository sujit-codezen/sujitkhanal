from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('detail/<int:pk>/',views.ProjectDetailView.as_view(), name='project_detail'),
    path('search/',views.SearchResultView.as_view(), name='search_project')
]