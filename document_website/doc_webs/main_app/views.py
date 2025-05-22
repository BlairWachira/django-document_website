from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import document
from django.db.models import Q

def sign_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user) 
            return redirect('dashboard')

    return render(request, 'sign.html')


def login_user (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    username = request.session.get('username', '')
    documents = document.objects.all()
    return render(request, 'dashboard.html', {'username': username,'documents': documents})

def search_results(request):
    query = request.GET.get('q')
    results = document.objects.filter(Q(title__icontains=query)) if query else []
    return render(request, 'search_results.html', {'documents': results, 'query': query})