from django.db import models

class Product(models.Model):
    prodid=models.CharField(max_length=10,unique=True)
    prodname=models.CharField(max_length=30)
    brand=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    description=models.TextField() 
    rate=models.IntegerField()
    category=models.CharField(max_length=20)
    objects=models.Manager()
    def __str__(self):
        return self.prodname
