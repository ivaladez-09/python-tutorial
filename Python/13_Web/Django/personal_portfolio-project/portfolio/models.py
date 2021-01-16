"""Add these classes to project_name/admin.py"""
from django.db import models


# ORM for the database
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # Make it optional -> blank=True

    def __str__(self):
        return self.title
