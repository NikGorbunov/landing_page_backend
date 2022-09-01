from django.db import models


class Project(models.Model):
    PREVIOUS = 'Previous'
    ONGOING = 'Ongoing'
    PROJECT_TYPE = [(PREVIOUS, 'Previous'), (ONGOING, 'Ongoing')]
    project_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    size = models.IntegerField()
    project_type = models.CharField(max_length=32, choices=PROJECT_TYPE)
    date_of_completion = models.DateTimeField(blank=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()
