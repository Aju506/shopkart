from django.urls import path
from . import views




app_name='shop'

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('cart',views.cart_page,name='cart'),

    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add_to_wishlist/<int:product_id2>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_wishlist/<int:wid>',views.remove_wishlist,name='remove_wishlist'),

    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart/<int:product_id>',views.add_to_cart,name="addtocart"),
    path('payment',views.payment,name='payment'),
    
]