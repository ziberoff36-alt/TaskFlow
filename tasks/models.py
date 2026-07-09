from django.db import models
from config import settings

class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='categories'
    )
    name = models.CharField(max_length=100)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                name='unique_category_per_user'
            )
        ]
    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Не начато'
        PROGRESS = 'progress', 'В процессе'
        DONE = 'done', 'Завершено'
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='tasks'
    )
    status = models.CharField(choices=Status, default=Status.NEW, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='tasks'
    )
    def __str__(self):
        return f'{self.title}: {self.id} - {self.user.username}'