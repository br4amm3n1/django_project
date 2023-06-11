from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}!')
        return redirect('news_home')
    else:
        form = UserRegisterForm()
    return render(request, 'REGpage/register.html', {'form': form})