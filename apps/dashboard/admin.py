from django.contrib import admin
from .models import Employee,Designation,Asset,Category,AssetAssign

# Register your models here.
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Asset)
admin.site.register(Category)
admin.site.register(AssetAssign)

class EmployeeAdmin(admin.ModelAdmin):
	def Action(self, obj):
		return format_html('')
	search_fields=['name','designation','status']
	list_display = ['name', 'email', 'designation', 'phone', 'address','status']
	list_display_links = None
	list_editable = ['status']
	list_per_page = 10