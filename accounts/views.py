from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm,LoginForm
# Create your views here.



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                first_name=data["first_name"],
                last_name=data["last_name"],
                username=data["user_name"],
                password=data["password_2"],
                email=data["email"],
                )
            return HttpResponse("با موفقیت ثبت نام شد.")
        else:
            return HttpResponse("خطای در ثبت نام رخ داده است.")
        
    else:
        form = RegisterForm()
    context = {"form":form}
    return render(request,"accounts/register.html",context)

            
    return render(request,"accounts/register.html")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request,username=User.objects.get(email=data["username"]),password=data["password"])
            except:
                user = authenticate(request,username=data["username"],password=data["password"])

            if user is not None:
                login(request,user)


                return HttpResponse("ورود با وفقیت بود.")
            else:
                return HttpResponse("این یوزر وجود ندارد")
        else:
            return HttpResponse("خطایی رخ داده است.")
        
    else:
        form = LoginForm()
    context = {"form":form}
    return render(request,"accounts/login.html",context)


def logout_view(reqauest):
    logout(reqauest)
    return HttpResponse("خروج از اکانت.") 

def profile_view(request):
    pass

def edit_profile_view(request):
    pass

def change_password_view(request):
    pass