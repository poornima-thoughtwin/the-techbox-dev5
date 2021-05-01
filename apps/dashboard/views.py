
from django.views.generic import View
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views import generic
from .models import Employee,Asset,Category,Designation,AssetAssign
from .forms import EmployeeForm,AssetForm,CategoryForm,DesignationForm,AssignAssetForm
#import pdb; pdb.set_trace()
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from tech_box.settings import MAIL
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import View

#......................................................................................................................
@method_decorator(login_required, name='dispatch')
class MyView(View):
    def get(self, request):
        employee = Employee.objects.all().count()
        asset = Asset.objects.all().count()
        assetassign = AssetAssign.objects.all().count()
        assetassign_list = AssetAssign.objects.filter(expire_date__lte=datetime.datetime.now())
        category = Category.objects.all().count()
        return render(request,'index.html', {'employee':employee,'asset':asset,'assetassign':assetassign,'category':category,'assetassign_list':assetassign_list})

class CreateEmployeeView(SuccessMessageMixin,CreateView):
    form_class = EmployeeForm
    # print(request.POST)
    model = Employee
    template_name = "employee/create_employee.html"
    success_url ="/employee/"
    success_message = "Employee was Created successfully"

# class CreateEmployeeView(View):

#     def get(self, request):
#         form = EmployeeForm
#         return render(request, 'employee/employee.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         try:
#             data = {}
#             emp_form = EmployeeForm(request.POST, request.FILES)
#             print(request.POST),
#             print(request.FILES)
#             if emp_form.is_valid():
#                 emp_form.save()
#                 messages.success(request, 'Employee Add success')
#                 newemp = Employee.objects.get(name=request.POST.get('name'))
#                 data['newemp'] = newemp

#                 return render(request, 'employee/new_row.html', data)
#             else:
#                 return HttpResponse("not valid")

#         except Exception as e:
#             print(e)
#         return render(request, 'employee/new_row.html')

# class EmployeeView(ListView):
#     form = EmployeeForm
#     model = Employee
#     #template_name = "employee/employee_list.html"
#     paginate_by = 3
#     queryset = Employee.objects.all()
#     template_name = "employee/employee.html"


class EmployeeView(View):

    #@method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        employees = Employee.objects.all()
        data['employee_list'] = employees
        data['form'] = EmployeeForm

        return render(request, 'employee/employee.html', data)


# class DeleteEmployeeView(SuccessMessageMixin,DeleteView):
#     model = Employee
#     template_name = "employee/employee_confirm_delete.html"
#     success_url ="/employee/"
#     success_message = "Employee was Deleted successfully"


class DeleteEmployeeView(View):

    def post(self, request):
        employee_id = request.POST.get('id')
        print(employee_id)
        employee = Employee.objects.get(id=employee_id)

        employee.delete()

        return HttpResponseRedirect("/employee/")

class UpdateEmployeeView(SuccessMessageMixin,UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "employee/update_employee.html"
    success_url ="/employee/"
    success_message = "Employee was Updated successfully"


#....................................................................................

class AssetCreateView(SuccessMessageMixin,CreateView):
    form_class = AssetForm
    model = Asset
    template_name = "asset/create_asset.html"
    success_url ="/asset/"
    success_message = "Asset was Created successfully"


class AssetView(ListView):
    model = Asset
    template_name = "asset/asset.html"
    paginate_by = 3

# class AssetView(View):

#     #@method_decorator(login_required(login_url="/login/"))
#     def get(self, request):
#         data = {}
#         asset = Asset.objects.all()
#         print(asset)
#         data['asset_list'] = asset
#         data['form'] = AssetForm

#         return render(request, 'asset/asset.html', data)

# class AssetDeleteView(DeleteView):
#     model = Asset
#     template_name = "asset/asset_confirm_delete.html"
#     success_url ="/asset/"
#     success_message = "Asset was delete successfully"

class AssetDeleteView(View):

    def post(self, request):
        asset_id = request.POST.get('id')
        print(asset_id)
        asset = Asset.objects.get(id=asset_id)

        asset.delete()

        return HttpResponseRedirect("/asset/")


class AssetUpdateView(SuccessMessageMixin,UpdateView):
    form_class = AssetForm
    model = Asset
    template_name = "asset/update_asset.html"
    success_url ="/asset/"
    success_message = "Asset was Updated successfully"

#...................................................................................

class CategoryCreateView(View):
    def get(self,request):#show
        form = CategoryForm()
        messages.success(request,'Category successfully Deleted')
        return render(request,"category/create_category.html",{'form':form})
    def post(self,request):#submit
        form =CategoryForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect("/category/")


class CategoryView(View):
    def get(self,request):
        category = Category.objects.all()
        paginator=Paginator(category,3)
        page_number= request.GET.get('page')
        page_obj =paginator.get_page(page_number)
        return render(request,"category/category.html",{'category_list':category,'page_obj':page_obj})

# class CategoryDeleteView(View):
#     def get(self,request,id):
#         qureyset = Category.objects.filter(id=id).delete()
#         messages.success(request,'Category successfully Deleted')
#         return HttpResponseRedirect("/category/")

class CategoryDeleteView(View):

    def post(self, request):
        category_id = request.POST.get('id')
        print(category_id)
        category = Category.objects.get(id=category_id)

        category.delete()

        return HttpResponseRedirect("/category/")


class CategoryUpdateView(SuccessMessageMixin,UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = "category/category_update.html"
    success_url ="/category/"
    success_message = "Category was Updated successfully"

#.......................................................

class DesignationCreateView(View):
    def get(self,request):
        form = DesignationForm()
        messages.success(request,'AssetAssign Created Deleted')
        return render(request,"designation/designation_create.html",{'form':form})
    def post(self,request):
        form = DesignationForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect("/designation/")


class DesignationView(View):
    def get(self,request):
        designation = Designation.objects.all()
        paginator=Paginator(designation,2)
        page_number= request.GET.get('page')
        page_obj =paginator.get_page(page_number)
        return render(request,"designation/designation.html",{'designation_list':designation,'page_obj':page_obj})

class DesignationDeleteView(View):
    def get(self,request,id):
        qureyset = Designation.objects.get(id=id)
        qureyset.delete()
        messages.success(request,'Designation Deleted Deleted')
        return HttpResponseRedirect("/designation")


class DesignationUpdateView(SuccessMessageMixin,UpdateView):
    form_class = DesignationForm
    model = Designation
    template_name = "designation/designation_update.html"
    success_url ="/designation/"
    success_message = "designation was Updated successfully"

#...........................................................................

class SearchResultsView(ListView):
    model = Employee
    template_name = 'employee/employee.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # new
        employee_list = Employee.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
        return employee_list

#...................................................................

class AssetAssignView(ListView):
    model = AssetAssign
    paginate_by = 3
    template_name = "assetassign/asset_assign.html"

class AssetAssignCreateView(View):
    def get(self,request):#show
        form = AssignAssetForm()
        messages.success(request,'AssetAssign Created successfully')

        return render(request,"assetassign/create_assetassign.html",{'form':form})
    def post(self,request,*args, **kwargs):#submit
        form = AssignAssetForm(request.POST or None)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            asset = form.cleaned_data['asset']
            print(asset)
            employee = str(employee)
            asset = str(asset)
            print(employee)
            form.save()
            MAIL(employee,asset)
            messages.success(request,'AssetAssign successfully Created')
        return HttpResponseRedirect("/assetassign/")
   

class AssetAssignDeleteView(View):
    def get(self,request,id):
        qureyset = AssetAssign.objects.get(id=id)
        qureyset.delete()
        messages.success(request,'AssetAssign successfully Deleted')
        return HttpResponseRedirect("/assetassign")
    

#......................................................................................

# @login_required
# def show_mutual_fund(request):
#     user = User.objects.get(username = request.user)   
#     funds = Mutual_Fund.objects.filter(user__pk=user.id)
#     paginator=Paginator(funds,6)
#     page_number= request.GET.get('page')
#     page_obj =paginator.get_page(page_number)
#     return render(request,'dashboard/show_mutual_fund.html',{'page_obj':page_obj})



# def user_profile(request):
#     # breakpoint()
#     if request.method=="POST":
#         username =  request.POST.get("username")
#         print(username)
#         password = request.POST.get("password")
#         email = request.POST.get("email")    
#         contact_number = request.POST.get("contact_number")
#         city = request.POST.get("city")
#         about = request.POST.get("about")
#         gender = request.POST.get("gender")
#         occupation =request.POST.get("occupation")
#         dob = request.POST.get("dob")
#         user_check = User.objects.filter(username=username).first()
#     if user_check is None:

#         # breakpoint()
#         user = User(username=username,email=email)
#         user.set_password(password)
#         user.save()
#         img = request.POST.get('profile_pic')
#         reg = user_profile.objects.create(user=user, 
#                                         contact_number=contact_number, 
#                                         city=city, 
#                                         about=about, 
#                                         gender=gender, 
#                                         occupation=occupation,
#                                         profile_pic=img)
#         return redirect('home')


#     elif user_check is not None:
#         return JsonResponse({"status":"user alredy exist"})
#     else:
#         return render(request,"registration/user_profile.html")

# #.........................................................................................


# @method_decorator(login_required, name='dispatch')
# class CategoryDeleteView(SuccessMessageMixin,generic.DeleteView):
#     model = Category
#     success_message = "Category was Deleted successfully"
#     success_url = reverse_lazy('dashboard:view_category')
#     def get(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return self.delete(request, *args, **kwargs)



 # path('api/employee/create',api_views.EmployeeCreateApi.as_view(),name='api_employee_create'),
    # path('api/employee/list',api_views.EmployeeListApi.as_view(),name='api_employee_list'),
    # path('api/employee/update/<int:pk>',api_views.EmployeeUpdateApi.as_view(),name='api_employee_update'),
    # path('api/employee/delete/<int:pk>',api_views.EmployeeDeleteApi.as_view(),name='api_employee_delte'),

    