from django.shortcuts import render
from projects.models import Project, ProjectImage, ProgrammingLanguage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def project_list(request):
    types = request.GET.get('types')
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    
    object_list = Project.objects.all()
    
    if types:
        object_list = object_list.filter(project_type=types)
    if q:
        object_list = object_list.filter(Q(project_name__icontains=q))
    if tag:
        object_list = object_list.filter(language_used__name=tag)
    
    paginator = Paginator(object_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    latest_project = Project.objects.all().order_by('-created')[:4]
    language = ProgrammingLanguage.objects.all()
    
    return render(request, 'projects/project.html', {
        'projects': page_obj,
        'latest_project': latest_project,
        'language': language,
        'types': types,
        'q': q,
        'tag': tag
    })

class ProjectDetailView(DetailView):
    # specify the model to use
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'

    def get_context_data(self, *args, **kwargs):
        page_title = "Details"
        context = super(ProjectDetailView,
             self).get_context_data(*args, **kwargs)
        context['page_title'] = page_title
        context['project_image'] = ProjectImage.objects.filter(project__id=self.kwargs['pk'])
        related_project = Project.objects.filter(project_type=self.object.project_type).exclude(id=self.kwargs['pk'])[:3]
        context['related_project'] = related_project
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