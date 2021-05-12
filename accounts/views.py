from django.shortcuts import render
from .models import Login
# from .models import Account
# Create your views here.

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    data = Login(username=username,password=password)
    data.save()
    return render(request,'registration/login.html')

""" def users(request):

     return render(request,'registration/users.html',{'Users':Account.objects.all()})

 def signUp(request):

     return render(request,'registration/signUp.html',)"""
