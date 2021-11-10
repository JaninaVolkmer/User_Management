from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import UserForm

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


"""
if view is displayed by browser, will be accessed by GET method
- register.html will be rendered
- last arguments of .render() is a context = contains UserForm
elif form is submitted, view is accessed by POST method
    - Django will create a user
    - new UserForm is created using submitted values
        - contained in request.POST object
"""


def register(request):
    if request.method == 'GET':
        return render(
            request, 'users/register.html',
            {'form': UserForm}
        )
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))
