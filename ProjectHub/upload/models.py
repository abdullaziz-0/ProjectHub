from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('AI', 'AI'),
        ('Network', 'Network'),
        ('Security', 'Security'),
        ('Web Development', 'Web Development'),
        ('Robotics', 'Robotics'),
    ]
    
    BRANCH_CHOICES = [
        ('CS', 'CS'),
        ('IT', 'IT'),
        ('COE', 'COE'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    video = EmbedVideoField(blank=True, null=True)
    githubURL = models.URLField()
    group_members = models.TextField()

    def __str__(self):
        return self.project_name
