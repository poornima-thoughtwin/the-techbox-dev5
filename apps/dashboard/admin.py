from django.contrib import admin
from .models import Employee,Designation,Asset,Category,AssetAssign

# Register your models here.
# admin.site.register(Employee)
# admin.site.register(Designation)
# admin.site.register(Asset)
# admin.site.register(Category)
# admin.site.register(AssetAssign)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	search_fields=['name','designation','status']
	list_display = ['name', 'email', 'designation', 'phone', 'address','status']
	list_display_links = None
	list_editable = ['status']
	list_per_page = 10

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_display = ['name']
	

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
	search_fields=['name','category','model_number','expire_date','availability']
	list_display =['name','category','model_number','expire_date','availability']
	list_display_links = None
	list_editable = ['availability']
	list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_display = ['name']
	

@admin.register(AssetAssign)
class AssetAssignAdmin(admin.ModelAdmin):
	search_fields=['employee','asset','expire_date']
	list_display =['employee','asset','expire_date']
	# list_display_links = None
	# list_editable = ['expire_date']
	# list_per_page = 10
