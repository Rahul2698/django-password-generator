from django.shortcuts import render
import random
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for i in range(length):
        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.GET.get('numbers'):
            characters.extend(list('0123456789'))
        if request.GET.get('special'):
            characters.extend(list('!@#$%^&*()'))
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
