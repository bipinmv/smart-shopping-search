from django.db import models
from django.contrib.auth.models import User
from smart_searchapp.models import Product
from django.core.validators import RegexValidator
from phone_field import PhoneField

# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,13}$', message="Should be in the format: '+91(10 digits)'")
    phone=models.CharField(validators=[phone_regex], max_length=13, blank=True)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    products=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)    
    date=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    ordered=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)
    total=models.DecimalField(default=0.00,max_digits=8,decimal_places=2)

    def __str__(self):
        return self.user.username
    
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)   
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True) 

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=200)

    def __str__(self):
        return self.subject
    
    
