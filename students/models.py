from django.db import models

# Create your models here.
from professor.models import assignments

class students_assignment(models.Model):
    file_submitted=models.FileField(null=True)
    submitted_on=models.DateTimeField(null=True)
    marks_reci=models.TextField(null=True)
    roll_number=models.TextField()
    file_name=models.TextField(null=True)
    assignments_id=models.TextField()
    # pass