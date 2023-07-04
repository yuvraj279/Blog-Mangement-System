from django.shortcuts import render
from django.http import HttpResponse  
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse('This is Home')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please Fill the form correctly')
        else:
            contact= Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your message has been Sent')
    return render(request,'home/contact.html') 

def about(request):
    messages.success(request,'This is about')
    return render(request,'home/about.html')