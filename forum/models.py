from django.db import models

# Create your models here.

class fmsg(models.Model):
    posted_by=models.TextField()
    content=models.TextField()

    def __str__(self):
        return self.posted_by