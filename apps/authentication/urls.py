from . import views

from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import  static
from django.conf import settings
from django.urls import path
from . import views 
#...........................................................................


urlpatterns = [
	path('', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('register/', views.RegistrationView.as_view(), name='register'),
    path('register/',views.myregister,name='register'),#fun
    #path('user_profile/', views.UserProfileView.as_view(),name="user_profile"),
    #path('user_profile/', views.UuserProfileUpdateView.as_view(),name="user_profile"),
    path('user_profile/',views.user_profile,name='user_profile'),#fun

]