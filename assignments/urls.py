from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.AssignmentFormView.as_view(), name='assignment_form'),
]