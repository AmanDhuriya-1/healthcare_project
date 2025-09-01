from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import InfoForm, SignUpForm
from .models import Info
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

@login_required
def add_info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('my_info')
    else:
        form = InfoForm()
    return render(request, 'core/add_info.html', {'form': form})

@login_required
def my_info(request):
    items = Info.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/my_info.html', {'items': items})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
