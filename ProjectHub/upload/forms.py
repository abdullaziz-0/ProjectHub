from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'category', 'branch', 'video', 'pdf_file', 'githubURL', 'group_members']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'video': forms.TextInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control-file', 'accept': '.pdf'}),
            'githubURL': forms.URLInput(attrs={'class': 'form-control'}),
            'group_members': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }
