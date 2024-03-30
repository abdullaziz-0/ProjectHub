from django.shortcuts import render, redirect
from .models import Project

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        pdf_file = request.FILES.get('pdf_file')
        
        if name and description and pdf_file:  # Simple validation
            project = Project(name=name, description=description, pdf_file=pdf_file)
            project.save()
            return redirect('home')
    return render(request, 'ProjectHub/upload.html', {})
