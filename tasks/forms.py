from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'description']
        labels = {
            'title': 'Название',
            'category': 'Категория',
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Необязательно'
            })
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Не выбрано'