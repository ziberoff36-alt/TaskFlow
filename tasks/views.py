from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.forms import TaskForm, CategoryForm
from tasks.models import Task, Category


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'Создание задачи'
        context['button_text'] = 'Создать'
        return context

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'Изменение задачи'
        context['button_text'] = 'Сохранить'
        return context

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'tasks/category_list.html'
    context_object_name = 'categories'
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'tasks/category_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return self.request.GET.get(
            'next',
            reverse_lazy('task_create')
        )