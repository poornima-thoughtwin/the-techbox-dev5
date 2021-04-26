from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from .models import user_profile
# from .forms import EmployeeForm,AssetForm,CategoryForm,DesignationForm
#import pdb; pdb.set_trace()
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
#............................................................................... Create your views here.

class LoginView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            message.success(request,'Logged In')
            print(user)
            if user is not None:
                return HttpResponseRedirect("index/")
            else:
                return HttpResponse("Inactive user.")
    
        else:
            return render(request,'registration/login.html')
    
    def get(self,request):
        forms = UserCreationForm()
        return render(request, 'registration/login.html', {'form': form})
                   
# class LoginView(View):
#     def post(self,request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = request.POST['username']
#             password = request.POST['password']
#             email = request.POST['email']             
#             user = authenticate(username=username,email=email)
#             user.set_password(password)
#             user.save()
#             messages.success(request,'incorrect')
#             return render(request, "registration/login.html", {"form": form})
#     def get(self,request):
#         form = UserCreationForm()
#         messages.success(request,'successfully')
#         return render(request, "registration/login.html", {"form": form})


def myregister(request):
    if request.method=="POST":
        username =  request.POST.get("username")
        password = request.POST.get("password")
        print(password)
        email = request.POST.get("email")    
        user_check = User.objects.filter(email=email).first()
        if user_check is None:
            user = User.objects.create_user(username,email,password)
        
            return redirect('/index/')
        elif user_check is not None:
            return HttpResponse("user already exist")
    else:
        return render(request, "registration/register.html")




def user_profile(request):
    if request.method=="POST":
        username =  request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        email = request.POST.get("email")    
        contact_number = request.POST.get("contact_number")
        city = request.POST.get("city")
        about = request.POST.get("about")
        gender = request.POST.get("gender")
        occupation =request.POST.get("occupation")
        dob = request.POST.get("dob")
        user_check = User.objects.filter(username=username).first()
        if user_check is None:
            user = User.objects.create_user(username,email,password)
            # user = User(username=username,email=email)
            # user.set_password(password)
            # user.save()
            img = request.POST.get('profile_pic')
            reg = user_profile.objects.create_user(user=user, 
                                            contact_number=contact_number, 
                                            city=city, 
                                            about=about, 
                                            gender=gender, 
                                            occupation=occupation,
                                            profile_pic=img)
            return redirect('home')


        elif user_check is not None:
            return JsonResponse({"status":"user alredy exist"})
    else:
        return render(request,"registration/user_profile.html")

#....................................................
