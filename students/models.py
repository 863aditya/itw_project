from django.db import models

# Create your models here.
from professor.models import assignments

class students_assignment(models.Model):
    file_submitted=models.FileField()
    
    pass