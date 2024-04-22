from django.shortcuts import render, redirect
from .models import Project

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        university=request.POST.get('university')
        video = request.POST.get('video', '')  
        pdf_file = request.FILES.get('pdf_file')
        linkedinURL=request.POST.get('linkedinURL')

        
        if name and description and category and pdf_file and university and linkedinURL:
            project = Project(name=name, description=description, category=category,university=university,video=video, pdf_file=pdf_file,linkedinURL=linkedinURL)
            project.save()
            return redirect('home') 
    return render(request, 'ProjectHub/upload.html', {})
