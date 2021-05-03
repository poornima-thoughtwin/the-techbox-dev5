
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
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView
import stripe
from django.conf import settings
#......................................................................................................................

class HomePageView(TemplateView):
    template_name = 'registration/home.html'


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)



@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'pen drive',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '100',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

class SuccessView(TemplateView):
    template_name = 'registration/success.html'


class CancelledView(TemplateView):
    template_name = 'registration/cancelled.html'


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




class EmployeeView(View):

    #@method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        employees = Employee.objects.all()
        data['employee_list'] = employees
        data['form'] = EmployeeForm

        return render(request, 'employee/employee.html', data)




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



