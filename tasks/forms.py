from django import forms
from tasks.models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category']
        labels = {
            'title': 'Название',
            'category': 'Категория',
        }
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['category'].empty_label = 'Не выбрано'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        labels = {
            'name': 'Название'
        }