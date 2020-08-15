from django.contrib import admin
from . models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields=['prodname','brand']
    list_filter=['category','brand']
    list_display=['prodname','rate']
    list_editable=['rate']

admin.site.register(Product,ProductAdmin)
