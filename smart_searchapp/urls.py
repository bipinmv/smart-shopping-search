from django.urls import path
from . import views

app_name='smart_searchapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('product?<int:id>/',views.product_detail,name='product'),
]