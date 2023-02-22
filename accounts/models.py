from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# from product.models import *
class User(models.Model):
    Phone_number=models.CharField(max_length=100,unique=True)
    email=models.EmailField()
    is_customer=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True)



    
    
class userProfileModel(models.Model):
    MALE='1'
    FEMALE='2'
    OTHERS='3'
    genderChoices=((MALE,'male'),(FEMALE,'female'),(OTHERS,'others'))
    owner=models.OneToOneField("User",on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Date_of_birth=models.DateField()
    Gender=models.CharField(max_length=100,choices=genderChoices,blank=True,null=True)
    image=models.ImageField(upload_to='profileImage/%Y/%m/%d/', default='defaultProduct.jpg')
    
class userloginotpModel(models.Model):
    owner=models.ForeignKey('User',on_delete=models.CASCADE)
    Otp=models.IntegerField()
    active=models.BooleanField()
    
class UserCartProductModel(models.Model):
    pending='1'
    Completed='2'
    statusChoices=((pending,'pending data'),(Completed,'completed'))
    owner=models.ForeignKey('User',on_delete=models.CASCADE)
    product=models.ForeignKey('Product.productMainModel',on_delete=models.CASCADE)
    status=models.BooleanField(choices=statusChoices,blank=True)
    
class UserCartModel(models.Model):
    owner=models.OneToOneField('User',on_delete=models.CASCADE)
    products=models.ManyToManyField("UserCartProductModel")
    price=models.FloatField()