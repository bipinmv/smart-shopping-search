from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
#from . import forms
from django.db.models import Q
from django.contrib import messages
from user.models import Wishlist


def index(request):
    query=request.GET.get('query')
    query_audio=request.GET.get('audioquery')
    query_video=request.GET.get('objquery')

    qs=Product.objects.all().order_by('?')
    if query!='' and query is not None:
        qs=qs.filter(
            Q(prodname__icontains=query) | Q(description__icontains=query) | 
            Q(brand__icontains=query) | Q(category__icontains=query)
            )
    elif query_audio!='' and query_audio is not None:
        qs=qs.filter(
            Q(prodname__icontains=query_audio) | Q(description__icontains=query_audio) | 
            Q(brand__icontains=query_audio) | Q(category__icontains=query_audio)
            )  
    elif query_video!='' and query_video is not None:
        qs=qs.filter(
            Q(prodname__icontains=query_video) | Q(description__icontains=query_video) | 
            Q(brand__icontains=query_video) | Q(category__icontains=query_video)
            )          

    return render(request,'smart_searchapp/index.html',{'products':qs})


def product_detail(request,id):
    prod=get_object_or_404(Product,id=id)
    check=False
    if request.user.is_authenticated:
        witem=Wishlist.objects.filter(user=request.user,product_id=prod)
        if witem.count()==0:
            check=True
        return render(request,'smart_searchapp/product.html',{'product':prod,'check':check,'witem':witem})    
    return render(request,'smart_searchapp/product.html',{'product':prod,'check':check})

