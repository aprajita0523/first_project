from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage
'''
print('hello')
def index(request):
    helpdict = {"help_insert":"help page"}# Create your views here.
    return render(request,"first_app1/help.html",context=helpdict)'''


def index(request):
    #return HttpResponse("<em>hello First Project</em>")
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request,"first_app1/index.html",context=date_dict)

print('hi')
def help(request):
    helpdict = {"help_insert":"help page"}# Create your views here.
    return render(request,"first_app1/help.html",context=helpdict)
