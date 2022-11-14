from django.db import models

# Create your models here.


class make_announcement(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

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
    file_assignment=models.TextField()
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
