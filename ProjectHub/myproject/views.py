from django.shortcuts import get_object_or_404, redirect, render
from upload.models import Project
from upload.forms import ProjectForm
from django.http import HttpResponseForbidden

def user_projects(request):
    user_projects = Project.objects.filter(user=request.user)    
    return render(request, 'ProjectHub/user_projects.html', {'user_projects': user_projects})

def projectName(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'ProjectHub/projects.html', {'project': project})

def delete_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('home')  

    if request.user == project.user:
        project.delete()
        return redirect('home')  
    else:
        return redirect('home')  

def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projectName', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'ProjectHub/project_form.html', {'form': form, 'project': project})
