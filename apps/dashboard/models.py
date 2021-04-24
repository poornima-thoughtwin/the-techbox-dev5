from django.db import models
from django.contrib.auth.models import User




class AssetAssign(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    asset = models.ForeignKey('Asset',on_delete=models.CASCADE)
    expire_date = models.DateTimeField()
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True,default="")
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True,default="")
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    model_number = models.CharField(max_length=100,null=True,blank=True,default="")
    availability =models.BooleanField(default=True)
    expire_date=models.DateTimeField()
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True,default="")
    email = models.EmailField(unique=True)
    designation = models.ForeignKey('Designation',on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,blank=True,default="")
    address = models.CharField(max_length=100,blank=True,null=True,default="")
    status =models.BooleanField(default=True)
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.email

class Designation(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True,default="")
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name



class notification(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True,null=True,default="")
    notification_type = models.CharField(max_length=100,blank=True,null=True,default="")
    Image = models.ImageField(blank=True,default="")
    description = models.TextField(blank=True,null=True,default="")
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
    def __str__(self):
        return self.title
