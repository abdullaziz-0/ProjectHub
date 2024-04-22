from django.db import models
from embed_video.fields import EmbedVideoField

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.TextField()
    university=models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    video = EmbedVideoField(blank=True, null=True) 
    linkedinURL=models.URLField()
    


    def __str__(self):
        return self.name
