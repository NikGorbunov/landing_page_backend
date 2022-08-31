from django.db import models


class PreviousProjects(models.Model):
    project_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    size = models.IntegerField()
    date_of_completion = models.DateTimeField(auto_now_add=True)


class OngoingProjects(models.Model):
    project_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    size = models.IntegerField()


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()
