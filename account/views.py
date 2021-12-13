from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)
                user.save()
                print("created")
        else:
            print("password not match")
            return redirect("register")
        return redirect("/")
    else:
        return render(request,'registration.html')


def ac_details(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalide login')
            return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


