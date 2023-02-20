from django.shortcuts import render
from projects.models import Project
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project.html'
    context_object_name = 'projects'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectListView,
             self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        object_list = Project.objects.all()
        return object_list

class ProjectDetailView(DetailView):
    # specify the model to use
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView,
             self).get_context_data(*args, **kwargs)
        return context
        # try:
        #     images = ProjectImage.objects.filter(project__id=self.kwargs['pk'])
        #     context['images'] = images
        #     return context
        # except:
        #     return HttpResponseRedirect('/')

class SearchResultView(ListView):
    model = Project
    template_name = 'projects/project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Project.objects.filter(
            Q(project_name__icontains=query)
        )
        return object_list