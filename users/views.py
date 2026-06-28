from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'users/register.html', {'form': form})
