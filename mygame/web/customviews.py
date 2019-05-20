from django.shortcuts import render
from django.conf import settings
from django.template import *

#Views set for out custom pages

def profilepage(request):
    return render(request, "profile.html")

def statspage(request):
    return render(request, "stats.html")

def pagetop(request):
    return render(request, "index.html")

def about(request):
    return render(request, "index.html")

def how2play(request):
    return render(request, "index.html")
