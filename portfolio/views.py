from django.shortcuts import render
from projects.models import Project

def index(request):
    projects = Project.objects.all().order_by('-created')[:8]
    title = "home"
    context = {
        'projects':projects,
        'title': title
    }

    return render(request, 'index.html', context)