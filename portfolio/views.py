from django.shortcuts import render
from projects.models import Project
from settings.models import MyDetail, Knowledge, Education, Experience, Skill
import requests
from django.http import HttpResponse

def index(request):
    projects = Project.objects.all().order_by('-created')[:4]
    knowledge = Knowledge.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    page_title = "Home"
    context = {
        'projects':projects,
        'page_title': page_title,
        'knowledge': knowledge,
        'education': education,
        'experience': experience,
        'skills': skills
    }

    return render(request, 'index.html', context)

def download_cv(request):
    my_details = MyDetail.objects.first()
    cloudinary_url = my_details.cv.url
    response = requests.get(cloudinary_url)
    
    if response.status_code == 200:
        # Prepare the file content for download
        file_content = response.content
        content_type = 'application/pdf'
        
        # Create the response to send the file to the user as an attachment
        response = HttpResponse(file_content, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="cv_sujitkhanal.pdf"'
        return response
    else:
        return HttpResponse("File not found.", status=404)