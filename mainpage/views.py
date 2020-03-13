from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from datetime import datetime
from django.core.exceptions import PermissionDenied
from .models import *
from django.contrib.auth import logout
# Create your views here.
def mainpage(request):

    return render (request , template_name= 'mainpage.html')

def test(request):
    return render (request , template_name='test.html')
    # return HttpResponse("<html><body>this is hello one </body></html>")

def login(request):
    logout(request)
    return render(request , template_name='login.html')
def signup(request):
    return render (request , template_name='signup.html')