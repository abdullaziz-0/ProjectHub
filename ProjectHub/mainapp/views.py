from django.shortcuts import render
from upload.models import Project

def home(request):
    selected_branch = request.GET.get('branch')

    if not selected_branch or selected_branch == 'All':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(branch=selected_branch)

    return render(request, 'ProjectHub/homepage.html', {'projects': projects})

