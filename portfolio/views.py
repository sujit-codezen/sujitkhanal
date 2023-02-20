from django.shortcuts import render
from projects.models import Project

def index(request):
    projects = Project.objects.all().order_by('-created')[:8]
    context = {
        'projects':projects,
    }

    return render(request, 'index.html', context)