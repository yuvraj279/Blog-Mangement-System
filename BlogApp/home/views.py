from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is Home')

def contact(request):
    return HttpResponse('This is Contact')

def about(request):
    return HttpResponse('This is About')