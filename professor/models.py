from django.db import models

# Create your models here.


class make_announcement(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

    def __init__(self,a1,a2,a3):
        self.title=a1
        self.content=a2
        self.date_posted=a3
    # pass

class exams(models.Model):
    title_exam=models.TextField()
    file_exam=models.FileField()
    deadline_exam=models.DateTimeField()
    message_exam=models.TextField()
    # pass
    def __str__(self):
        return self.title_exam



class assignments(models.Model):
    title_assignment=models.TextField()
    file_assignment=models.FileField()
    deadline_assignment=models.DateTimeField()
    message_assignment=models.TextField()
    # pass
    def __str__(self):
        return self.title_assignment


class publish_ppt(models.Model):
    file_publish=models.FileField()
    message_publish=models.TextField()
    # pass
    def __str__(self):
        return self.file_publish
