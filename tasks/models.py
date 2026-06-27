from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
