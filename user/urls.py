from django.urls import path
from . import views

app_name='user'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('add-to-cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('delete_from_cart/<int:id>/',views.delete_from_cart,name='delete_from_cart'),
    path('profile/',views.profile,name='profile'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('add-to-wishlist/<int:id>',views.add_to_wishlist,name='add_to_wishlist'),
    path('add_to_wishlist/<int:id>',views.add_to_wishlist_before_login,name='add-to-wishlist'),
    path('remove-from-wishlist/<int:id>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('remove/<int:id>',views.remove_from_wishlist_prodpage,name='remove'),
    path('feedback/',views.feedback,name='feedback')
]