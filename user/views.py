from django.shortcuts import render,redirect,get_object_or_404
from .models import UserInfo,Cart,Wishlist,Feedback
from .forms import UserForm,UserInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from smart_searchapp.models import Product
from django.utils import timezone
#from django.views.decorators.cache import cache_control


# Create your views here.
def register(request):

    registered=False
    if request.user.is_authenticated:
        return redirect('smart_searchapp:index')
    else:

        if request.method=='POST':
            user_form=UserForm(request.POST)
            user_info=UserInfoForm(request.POST)

            if user_form.is_valid() and user_info.is_valid():
                user=user_form.save()
                user.set_password(user.password)
                user.save()

                info=user_info.save()
                info.user=user
                info.save()

                #name=user_info.cleaned_data.get('name')
                #messages=success(request,'Account created successfully for' + name)

                registered=True
                return redirect('user:login')

            else:
                print(user_form.errors,user_info.errors)
        else:
            user_form=UserForm()
            user_info=UserInfoForm()

        return render(request,'user/register.html',{'user_form':user_form,'user_info':user_info,'registered':registered})

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userlogin(request):
    
    if request.user.is_authenticated:
        return redirect('smart_searchapp:index')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request,username=username,password=password)
            if user:
                if user.is_superuser:
                    login(request,user)
                    return redirect('admin:index')
                elif user.is_active:
                    login(request,user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:    
                        return redirect('smart_searchapp:index')
            else:
                messages.info(request,'Invalid credential')

        return render(request,'user/login.html')     

@login_required(login_url='user:login')
def userlogout(request):
    logout(request)
    return redirect('smart_searchapp:index')   

@login_required(login_url='user:login')
def cart(request):
    citem=Cart.objects.filter(user=request.user)
    subtotal=0
    if citem:
        for rate in citem:
            subtotal+=rate.products.rate
    return render(request,'user/cart.html',{'citem':citem,'subtotal':subtotal})    

@login_required(login_url='user:login')
def add_to_cart(request,id):
    itemid=get_object_or_404(Product,id=id)
    item=Cart.objects.filter(user=request.user,products_id=itemid)

    if item.count()==0:
        cart_item=Cart.objects.create(user=request.user,products=itemid,ordered=False)
        messages.info(request,"One item has been added to your cart") 
        return redirect("user:cart")
    else:
        messages.info(request,"Item already exists in the cart") 
        return redirect("user:cart")
    #cart_query=Cart.objects.filter(user=request.user,ordered=False)
    
    """if cart_query.exists():
        cartcheck=cart_query
        # check if the item is in the cart
        if cartcheck.products.filter(id=itemid).exists():
            cart_item=Cart.objects.create(user=request.user,products=itemid,ordered=False)
            cart_item.quantity+=1
            cart_item.save()
            messages.info(request,"Item quantity has been updated") 
            return redirect("user:cart")
        else:
            cart_item=Cart.objects.create(user=request.user,products=itemid,ordered=False)
            cart_item.save()
            messages.info(request,"This item has been added to your cart") 
            return redirect("user:cart")
    else:
            cart_item=Cart.objects.create(user=request.user,products=itemid,ordered=False)
            cart_item.save()
            messages.info(request,"This item has been added to your cart") 
            return redirect("user:cart") """

    """if cart_query.exists():
        cart=cart_query
        # check if the item is in the cart
        if cart.products.filter(id=item.id).exists():
            cart_item.quantity+=1
            cart_item.save()
            messages.info(request,"Item quantity has been updated")
            return redirect("user:cart")
        else:
            cart.add(cart_item)
            cart.save()
            messages.info(request,"This item has been added to your cart") 
            return redirect("user:cart")"""


@login_required(login_url='user:login')
def delete_from_cart(request,id):
    cartdel=Cart.objects.get(id=id).delete()
    #messages.success(request,'One item has been removed from cart')
    return redirect("user:cart")

@login_required(login_url='user:login')    
def profile(request):
    return render(request,'user/profile.html')

@login_required(login_url='user:login')
def wishlist(request):
    witem=Wishlist.objects.filter(user=request.user)
    return render(request,'user/wishlist.html',{'witem':witem})

@login_required(login_url='user:login')
def add_to_wishlist(request,id):
    itemid=get_object_or_404(Product,id=id)
    item=Wishlist.objects.filter(user=request.user,product_id=itemid)
    if item.count()==0:
        wishlist_item=Wishlist.objects.create(user=request.user,product=itemid)
        messages.info(request,"Added to your wishlist") 
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        messages.error(request,"Item already exists in your wishlist")  
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))     

@login_required(login_url='user:login')
def add_to_wishlist_before_login(request,id):
    itemid=get_object_or_404(Product,id=id)
    item=Wishlist.objects.filter(user=request.user,product_id=itemid)
    if item.count()==0:
        wishlist_item=Wishlist.objects.create(user=request.user,product=itemid)
        messages.info(request,"Added to your wishlist") 
        return redirect('user:wishlist')
    else:
        messages.error(request,"Item already exists in your wishlist")  
        return redirect('user:wishlist')           

@login_required(login_url='user:login')
def remove_from_wishlist(request,id):
    wdelete=Wishlist.objects.get(id=id).delete()
    return redirect('user:wishlist')

@login_required(login_url='user:login')
def remove_from_wishlist_prodpage(request,id):
    wdelete=Wishlist.objects.get(id=id).delete()
    messages.info(request,"Removed from your wishlist") 
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))      

@login_required(login_url='user:login')
def feedback(request):
    if request.method=='POST':
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        feed=Feedback.objects.create(user=request.user,subject=subject,message=message)
        messages.info(request,'Your message has been sent')
    return render(request,'user/profile.html')   
       

