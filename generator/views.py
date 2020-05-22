from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    thepassword = ''
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
        
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
        
    for x in range(length):
        thepassword+= random.choice(characters)
        
    return render(request,'generator/password.html',{'password':thepassword})
