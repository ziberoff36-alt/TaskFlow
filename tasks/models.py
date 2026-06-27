from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Status(models.TextChoices):
    NEW = 'new', 'Не начато'
    PROGRESS = 'progress', 'В процессе'
    DONE = 'done', 'Завершено'

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tasks')
    status = models.CharField(choices=Status, default=Status.NEW, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
