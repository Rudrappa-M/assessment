from django.db import models
# Create your models here.

    
    
class productMainModel(models.Model):
    Title=models.CharField(max_length=200)
    Description=models.TextField()
    Unique_id=models.CharField(max_length=100,unique=True)
    Price=models.FloatField()


class productImageModel(models.Model):
    product=models.ForeignKey("productMainModel", on_delete=models.CASCADE)
    productimage=models.ImageField(upload_to='profileImage/%Y/%m/%d/', default='defaultProduct.jpg')
    
    
    
    
    