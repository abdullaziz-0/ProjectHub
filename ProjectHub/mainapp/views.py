from django.shortcuts import render,redirect
from upload.models import Project
def home(request):
    projects = Project.objects.all() 
    return render(request, 'ProjectHub/homepage.html', {'projects': projects})

