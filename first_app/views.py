from django.shortcuts import render
from django.http import HttpResponse

print('hello')
def index(request):
    return HttpResponse("<em>My Second Project</em>")

print('hi')
def help(request):
    helpdict = {'help_insert':'help page'}# Create your views here.
    return render(request,'first_app/help.html',context=helpdict)
