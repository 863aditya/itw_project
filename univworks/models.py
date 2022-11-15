from django.db import models

# Create your models here.
class students(models.Model):
    roll=models.TextField()
    email=models.TextField()
    first_name=models.TextField()
    last_name=models.TextField()
    password=models.TextField()
    username=models.TextField()
    def __str__(self):
        return self.roll


