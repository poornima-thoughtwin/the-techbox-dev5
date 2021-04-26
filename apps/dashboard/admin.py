from django.contrib import admin
from .models import Employee,Designation,Asset,Category,AssetAssign

# Register your models here.
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Asset)
admin.site.register(Category)
admin.site.register(AssetAssign)

# class Employee(admin.ModelAdmin):
#     list_display = ['name', 'email', 'designation', 'phone', 'address','status']
#     list_filter = ('name', 'designation','status') 
