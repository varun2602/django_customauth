from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse 
from . import models


@login_required(login_url= 'login')
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
@csrf_exempt   
def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        about = request.POST.get('about')

        try:
            user_check = models.CustomUser.objects.get(email =  email)
            return HttpResponse('User already exists')
        except models.CustomUser.DoesNotExist:
            user = models.CustomUser.objects.create_user(email = email, user_name = user_name, password = password, about = about)
            return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_check = models.CustomUser.objects.get(email = email)
            authenticated_user = authenticate(request, email = email, password = password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Invalid credentials')
        except models.CustomUser.DoesNotExist:
            return HttpResponse('User does not exists')
        

def logout_views(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

