from curses.ascii import HT
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from engine.models import Article







#User Registration
def registration(request):
    #return HttpResponse("<h2>Hospital Management System<h2>")
    #passing render and request
    #request is passed for later usage
    #we can also pass an data dicetionary
    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        
       

        if password1==password2:
                
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'This User Name Is Already Taken')
                return redirect('accounts/registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This Email Is Already Taken')
                return redirect('/accounts/registration')
            else:
                    user=User.objects.create_user(username=username,first_name=first_name,email=email,last_name=last_name,password=password1)
                    user.save()
                    return redirect("/accounts")
        else:
            messages.info(request,'Password Mismatch,Check Again')
            return redirect('/accounts/registration')
        
        

    
    else:
    
        return render(request,'registration.html')



#Login Functionality---------------------------------
def login(request):

    if request.method=='POST':
      
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/accounts')

        
       

        
        


        #saving data

    
    else:
        return render(request,'login.html')

#User Log Out Functionality 

def logout(request):
    auth.logout(request)
    return redirect("/")


def home(request):
    return redirect("/")


def userarticle(request):
    if request.user.is_authenticated:
            username = request.user.username
            article_list=Article.objects.filter(author=username)
            context={'articles':article_list}
            return render(request,'userarticle.html',context)