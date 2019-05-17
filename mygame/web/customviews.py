from django.shortcuts import render
from django.conf import settings
from django.template import *

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

# Function to determine if page is index. If page is index, then options #page-top, #about, #how2play, and #stats return with none url value.
 #def isPageIndex():
#
#    if request.path != /index
#       urlPageTop = '/'
#       urlAbout = '/#about'
#       urlHow2Play = '/#how2play'
#       urlStats = '/#stats'
#    elseif:
#       urlPageTop = '#page-top'
##       urlAbout = '#about'
#       urlHow2Play = '#how2play'
#       urlStats = '#stats'
