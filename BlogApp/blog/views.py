from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('This is blog Home, we will keep all the blogs here')

def blogPost(request, slug):
    return HttpResponse(f'This is Blog Post: {slug}')
