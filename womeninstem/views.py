from django.shortcuts import render, HttpResponse, redirect
from womeninstem.models import FormData, StoryData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth import login as auth_login

# Create your views here.
def home(request):
    #return HttpResponse("This is my home page")
    return render(request, 'home.html')
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')
def womeninstem(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'womeninstem.html')
    stemdataorder = FormData.objects.all()
    
    return render(request,"womeninstem.html",{"stemdataorder":stemdataorder})


def form(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'form.html')
    #farmerbuyorder = FoodOrder.objects.all()
    stemdataorder = FormData.objects.all()
    if request.method=="POST":
        field=request.POST['field']
        name=request.POST['name']        
        work=request.POST['work']
        link=request.POST['link']
        achieve=request.POST['achieve']


        #print(firstname, lastname, country, state, city, address, pin, phone, productname, productID, quantity, msg)

        stemdata = FormData(field=field, name=name, work=work, link=link, achieve=achieve)  

        stemdata.save()
        return redirect('womeninstem')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    return render(request,"form.html",{"Stems":stemdataorder})


def sharestory(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'sharestory.html')
    storyorder = StoryData.objects.all()
    if request.method=="POST":
        namess=request.POST['namess']
        story=request.POST['story']        
        achievess=request.POST['achievess']
        vlink=request.POST['vlink']
        contact=request.POST['contact']


        #print(firstname, lastname, country, state, city, address, pin, phone, productname, productID, quantity, msg)

        storydata = StoryData(namess=namess, story=story, vlink=vlink, achievess=achievess, contact=contact)  

        storydata.save()
        return redirect('seestory')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    return render(request,"sharestory.html",{"Stories":storyorder})

def seestory(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'womeninstem.html')
    storyorder = StoryData.objects.all()
    
    return render(request,"seestory.html",{"storyorder":storyorder})


def handleSignup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=='POST':
        #Get parameters posted
        susername=request.POST['susername']
        email=request.POST['email']
        sname=request.POST['sname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

#    ''' #Check info eerors
#        if len(username)<10:
#            messages.error(request, " Your user name must be under 10 characters")
#            return redirect('signup')
#
#        if not username.isalnum():
#            messages.error(request, " User name should only contain letters and numbers")
#            return redirect('signup')
#        if (pass1!= pass2):
#             messages.error(request, " Passwords do not match")
#             return redirect('signup')'''

        #Create User
        myuser = User.objects.create_user(susername, email, pass1)
        myuser.full_name=sname
        myuser.save()
        messages.success(request, "Your account has been successfully created")

    
        return redirect('handleLogin')


def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        username=request.POST['username'] 
        pass3=request.POST['pass3']

        user=authenticate(username=username, password=pass3)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')
    
    
    #return HttpResponse('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')

