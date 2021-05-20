from django.contrib import admin
from django.urls import path,include
from . import views 
from rest_framework.views import APIView 
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from django.conf.urls import url
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import  static
from django.conf import settings
from django.urls import path,include
from . import views 
from django.contrib import admin
from django.urls import path,include
from dashboard.api_views import CategoryList,CategoryDetail,DesignationDetail,DesignationList,AssetList,AssetDetail,EmployeeDetail,EmployeeList,AssetAssignDetail,AssetAssignList
from django.conf import settings
# from django.contrib.auth import views
# from .serializers import *
from dashboard import views

#>>>>>>
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView 
#..............................................................................................
urlpatterns = [
    path('admin/', admin.site.urls),

	path('search/',views.SearchResultsView.as_view(),name="search"),
	path('index/', views.MyView.as_view(),name="index"),
	path('employee/', views.EmployeeView.as_view(),name="employee"),
    path('create_employee/',views.CreateEmployeeView.as_view(),name='create_employee'),
    path('delete_employee/',views.DeleteEmployeeView.as_view(),name='delete_employee'),
    path('update_employee/<int:pk>',views.UpdateEmployeeView.as_view(),name='update_employee'),
#........................................................................
	path('asset/', views.AssetView.as_view(),name="asset"),
    path('create_asset/',views.AssetCreateView.as_view(),name='create_asset'),
    path('delete_asset/',views.AssetDeleteView.as_view(),name='delete_asset'),
    path('update_asset/<int:pk>',views.AssetUpdateView.as_view(),name='update_asset'),
#....................................................................................................
    path('category/', views.CategoryView.as_view(),name="category"),
    path('create_category/',views.CategoryCreateView.as_view(),name='create_category'),
    path('delete_category/',views.CategoryDeleteView.as_view(),name='delete_category'),
    path('update_category/<int:pk>',views.CategoryUpdateView.as_view(),name='update_category'),
#.........................................................................................
    path('designation/', views.DesignationView.as_view(),name="designation"),
    path('create_designation/',views.DesignationCreateView.as_view(),name='create_designation'),
    path('delete_designation/',views.DesignationDeleteView.as_view(),name='delete_designation'),
    path('update_designation/<int:pk>',views.DesignationUpdateView.as_view(),name='update_designation'),
#........................................................................................
    path('assetassign/', views.AssetAssignView.as_view(),name="assetassign"),
    path('create_assetassign/', views.AssetAssignCreateView.as_view(),name="create_assetassign"),
    path('delete_assetassign/', views.AssetAssignDeleteView.as_view(),name="delete_assetassign"),
    #path('api/login_user/', TokenObtainPairView.as_view(), name='login user'),
    path('api/asset/list', AssetList.as_view(),name='api_asset_list'),
    path('api/asset/create/',AssetList.as_view(),name='api_create_asset'),
    path('api/asset/delete/<int:pk>',AssetDetail.as_view(),name='api_asset_delete'),
    path('api/asset/update/<int:pk>',AssetDetail.as_view(),name='api_asset_update'),

    path('api/employee/list', EmployeeList.as_view(),name='api_employee_list'),
    path('api/employee/create/',EmployeeList.as_view(),name='api_employee_create'),
    path('api/employee/delete/<int:pk>',EmployeeDetail.as_view(),name='api_employee_delete'),
    path('api/employee/update/<int:pk>',EmployeeDetail.as_view(),name='api_employee_update'),


    path('api/assetassign/list', AssetAssignList.as_view(),name='api_assetassign_list'),
    path('api/assetassign/create/',AssetAssignList.as_view(),name='create_assetassign_list'),
    path('api/assetassign/delete/',AssetAssignDetail.as_view(),name='api_delete_assetassign'),
    path('api/assetassign/update/<int:pk>',AssetAssignDetail.as_view(),name='api_update_assetassign'),

    path('api/designation/list', DesignationList.as_view(),name='api_designation_list'),
    path('api/designation/create/',DesignationList.as_view(),name='api_designation_create'),
    path('api/designation/delete/<int:pk>',DesignationDetail.as_view(),name='api_delete_designation'),
    path('api/designation/update/<int:pk>',DesignationDetail.as_view(),name='api_update_designation'),
    
    path('api/category/list', CategoryList.as_view(),name='api_category_list'),
    path('api/category/create/',CategoryList.as_view(),name='api_category_create'),
    path('api/category/delete/<int:pk>',CategoryDetail.as_view(),name='api_category_delete'),
    path('api/category/update/<int:pk>',CategoryDetail.as_view(),name='api_category_update'),
    path('home/', views.HomePageView.as_view(), name='home'),
    # path('config/', views.stripe_config),
    # path('create-checkout-session/', views.create_checkout_session), 
    # path('success/', views.SuccessView.as_view()),
    # path('cancelled/', views.CancelledView.as_view()), 
    # path('charge/', views.ChargeView, name='charge'),
    # path('test/', views.HomePageView.as_view(), name='test'),
    path('charge/', views.charge, name='charge'),
    path('api/category/', views.CategoryAPIView.as_view())


] 



