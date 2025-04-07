from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View



# Create your views here.
class Register(View):
    def get(self, request):
        next_page = request.GET.get('next')
        return render(request, 'register.html',context={'next': next_page})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Registration successful!")
        next_page = request.GET.get('next')
        if next_page and next_page != "None":
            return redirect(next_page)
        return redirect('home')

class Login(View):
    def get(self, request):
        next = request.GET.get('next')
        return render(request, 'login.html',context={'next': next})

    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            next_page = request.GET.get('next')
            if next_page and next_page != "None":
                return redirect(next_page)
            return redirect('home')

        except Exception as e:
            messages.error(request, "invalid username or password")
            return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')
