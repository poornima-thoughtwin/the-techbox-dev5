from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import  static
from django.conf import settings
from django.urls import path
from . import views 

#..............................................................................................
urlpatterns = [
	path('search/',views.SearchResultsView.as_view(),name="search"),
	path('index/', views.MyView.as_view(),name="index"),
	path('employee/', views.EmployeeView.as_view(),name="employee"),
    path('create_employee/',views.CreateEmployeeView.as_view(),name='create_employee'),
    path('delete_employee/<int:pk>',views.DeleteEmployeeView.as_view(),name='delete_employee'),
    path('update_employee/<int:pk>',views.UpdateEmployeeView.as_view(),name='update_employee'),
#........................................................................
	path('asset/', views.AssetView.as_view(),name="asset"),
    path('create_asset/',views.AssetCreateView.as_view(),name='create_asset'),
    path('delete_asset/<int:pk>',views.AssetDeleteView.as_view(),name='delete_asset'),
    path('update_asset/<int:pk>',views.AssetUpdateView.as_view(),name='update_asset'),
#....................................................................................................
    path('category/', views.CategoryView.as_view(),name="category"),
    path('create_category/',views.CategoryCreateView.as_view(),name='create_category'),
    path('delete_category/<int:id>',views.CategoryDeleteView.as_view(),name='delete_category'),
    path('update_category/<int:pk>',views.CategoryUpdateView.as_view(),name='update_category'),
#.........................................................................................
    path('designation/', views.DesignationView.as_view(),name="designation"),
    path('create_designation/',views.DesignationCreateView.as_view(),name='create_designation'),
    path('delete_designation/<int:id>',views.DesignationDeleteView.as_view(),name='delete_designation'),
    path('update_designation/<int:pk>',views.DesignationUpdateView.as_view(),name='update_designation'),
#........................................................................................
    path('assetassign/', views.AssetAssignView.as_view(),name="assetassign"),
    path('create_assetassign/', views.AssetAssignCreateView.as_view(),name="create_assetassign"),
    path('delete_assetassign/<int:id>', views.AssetAssignDeleteView.as_view(),name="delete_assetassign"),

#..........................................................................
    #path('user_profile/', views.UserProfileView.as_view(),name="user_profile"),
    #path('user_profile/', views.UuserProfileUpdateView.as_view(),name="user_profile"),
    #path('user_profile/',views.user_profile,name='user_profile'),#fun

]





