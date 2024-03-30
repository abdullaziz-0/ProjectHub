from django.db import models

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name