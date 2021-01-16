"""Add these classes to project_name/admin.py"""
from django.db import models


# ORM for the database
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title
