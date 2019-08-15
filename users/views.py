from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import NewUserForm
# Create your views here.


def registeruser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your login created {username}')
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'user/register.html', {'form': form})
