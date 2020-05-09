from django.shortcuts import render
from django.http import HttpResponse
'''
print('hello')
def index(request):
    helpdict = {"help_insert":"help page"}# Create your views here.
    return render(request,"first_app1/help.html",context=helpdict)'''


def index(request):
    return HttpResponse("<em>hello First Project</em>")

print('hi')
def help(request):
    helpdict = {"help_insert":"help page"}# Create your views here.
    return render(request,"first_app1/help.html",context=helpdict)
