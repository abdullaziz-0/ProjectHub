from django.shortcuts import render
from upload.models import Project
def home(request):
    projects = Project.objects.all() 
    return render(request, 'ProjectHub/homepage.html', {'projects': projects})

