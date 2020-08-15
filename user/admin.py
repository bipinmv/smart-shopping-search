from django.contrib import admin
from . models import UserInfo,Cart,Wishlist,Feedback
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Feedback)