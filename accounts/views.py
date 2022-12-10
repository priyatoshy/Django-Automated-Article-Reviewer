# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from engine.models import Article
from .forms import CustomProfileCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .decorators import unauthneticated_user

#login
def loginUser(request):
    page='login'
    context={"page":page}
    if request.user.is_authenticated==False:

        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            try:
                User.objects.get(username=username)
                user=authenticate(request,username=username,password=password)

                if user!=None:
                #authenticated and session added
                    login(request,user)
                    return redirect("/")
                else:
                    messages.error(request,"😵Username or Password is incorrect")
            except:
                messages.error(request,"😵Username doesnt't exist")
    else:
        return redirect("/")
        
    

            
    return render(request,'accounts/login_register.html',context)

#logout
def logoutUser(request):
    #deletes the session
    logout(request)
    messages.info(request,"🙋Successfully Logged Out")
    return redirect("login")




#show profile
@login_required(login_url="login")
def show_profile(request,pk):

    profile=Profile.objects.get(id=pk)
    if request.user.profile==profile:
    

        if profile:
            articles=Article.objects.filter(writer=profile)
            if articles:
                context={"data":profile,"articles":articles}
            else:
                context={"data":profile,"articles":[]}
        else:
            context={}
        


        return render(request,"accounts/single_profile.html",context)
    else:
        return redirect("/")


#user registration

@unauthneticated_user
def registerUser(request):
            page='register'
            
            form=CustomUserCreationForm()
            
            if request.method=="POST":
                form=CustomUserCreationForm(request.POST,request.FILES)
                if form.is_valid():
                    #saving an instance before commiting
                    user=form.save(commit=False)
                    user.username=user.username.lower()
                    hold_object=User.objects.filter(email=user.email).first()
                    if hold_object:
                        print(f"\n\n\n{hold_object}\n\n\n")
                        messages.error(request,"Email Already Taken")
                        

                    else:
                        user.save()
                        messages.success(request,"User Created")
                        login(request,user)
                        return redirect(f"update-profile/{user.profile.id}")
                else:
                    messages.error(request,"An error has happened")
                    #the request with error must come to ths same page
                    #to show error
        
                    
            context={"page":page,"form":form}    
            return render(request,'accounts/login_register.html',context)



#UPDATE PROFILE----------------------------
@login_required(login_url="login")
def update_profile(request,pk):
    current_profile= request.user.profile
    profile=Profile.objects.get(id=pk)
    if current_profile==profile:
        
        form=CustomProfileCreationForm(instance=profile)
        

        if request.method=="POST":
            form=CustomProfileCreationForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                #saving an instance before commiting
                print(f"{request.POST}")
                form.save()
            
                messages.success(request,"User Updated")
                #return redirect("/")
            else:
                messages.error(request,"An error has happened")
                #the request with error must come to ths same page
                #to show error
                return redirect("/")
   
            
        context={"form":form}    
        return render(request,'accounts/edit_profile.html',context)
            


    else:
        messages.warning(request,"FORBIDDEN REQUEST")
        return redirect("/")









  