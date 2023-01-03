from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
# Create your views here.
def signup(request):
    return render(request, 'signup.html')
    
def login(request):
    return render(request, 'login.html')
    