from django.shortcuts import render,redirect
from django.http import HttpResponse  
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post


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

def search (request):
    query=request.GET['query']
    allPost=Post.objects.filter(title__icontains=query)
    params={'allPost':allPost,'query':query }
    return render(request, 'home/search.html',params)
    # return HttpResponse('This is search')

def handleSignup(request):
    if(request.method=='POST'):
        # Get The post paramaters
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # Checks for erronus inputs
        if len(username) > 10:
            messages.error(request, "User name must be under 10 Characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "User name must be Alpha Numeric")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request, "Passwords Do not match")
            return redirect('home')
        # Create the user 
        myuser=User.objects.create_user(username, email , pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request, "Your account has been successfully Created ")
        return redirect('home')
    else:
        return HttpResponse('404- Not Found!!')
    
def handleLogin(request):
    loginusername=request.POST['loginusername']
    loginpassword=request.POST['loginpassword']

    user=authenticate(username=loginusername, password=loginpassword)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return redirect('home')
    else:
        messages.error(request,"Invalid Credentails")
        return redirect('home')
    
    # return HttpResponse('This is login')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')
    # return HttpResponse('This is Log Out')