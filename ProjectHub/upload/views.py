from django.shortcuts import render, redirect
from .forms import ProjectForm

def upload(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'ProjectHub/upload.html', {'form': form})
