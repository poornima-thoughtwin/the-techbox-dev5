from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20,blank=True,default="")
    profile_pic =models.ImageField(upload_to ="userprofiles",null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    about = models.TextField(blank=True,null=True,default="")
    gender = models.CharField(max_length=250,default="Male")
    occupation = models.CharField(max_length=250,null=True,blank=True,default="")
    dob = models.DateField(default=True)
    created_at  =models.DateTimeField(auto_now_add=True,null=True)
    updated_at  = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.user.username  