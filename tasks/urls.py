from django.urls import path
from django.contrib.auth.views import LogoutView
from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, CategoryCreateView, TaskDeleteView, \
    CategoryListView, CategoryUpdateView, CategoryDeleteView, TaskStatusView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('status/<int:pk>/', TaskStatusView.as_view(), name='task_status'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),
]