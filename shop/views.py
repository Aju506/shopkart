from django.http import JsonResponse
from django.shortcuts import render,redirect
from shop.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from .models import Cart
from .models import Product
from django.contrib.auth.decorators import login_required




# Create your views here.

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,'shop/index.html',{'products':products})


def cart_page(request):
   cart_items=Cart.objects.all()
   total_price=sum(item.products.original_price*item.product_qty for item in cart_items)
   total_price_per_item=[]
   grand_total=0
   for item in cart_items:
      item_total=item.products.original_price*item.product_qty
      total_price_per_item.append({'item':item,'total':'item_total'})
      grand_total+=item_total

      return render(request,'shop/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
   return render(request,'shop/cart.html')


def remove_cart(request,cid):
   cartitem=Cart.objects.get(id=cid)
   cartitem.delete()
   return redirect('/cart')





def add_to_cart(request,product_id):
    if request.method=='POST':
      qty=request.POST['quantity']
      product=Product.objects.get(id=product_id)
      cart_item,created=Cart.objects.get_or_create(products=product,product_qty=qty)
      if not created:
         cart_item.product_qty+=1
         cart_item.save()
         messages.success(request,"added to cart")
      return redirect('shop:cart')


@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'shop/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id2):
     product = Product.objects.get(id=product_id2)
     WishlistItem.objects.get_or_create(user=request.user, product=product)
    
     return redirect('shop:wishlist')

def remove_wishlist(request,wid):
   item=WishlistItem.objects.get(id=wid)
   item.delete()
   return redirect('shop:wishlist')
   
    

def logout_page(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request,'Logged out Successfully')
      return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
       return redirect("/")
    else:
     if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"shop/login.html")
 
     
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
       form=CustomUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,'Registration Success You Can Login Now..!')
          return redirect('/login')
    return render(request,'shop/register.html',{'form':form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/collections.html',{'catagory':catagory})

def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{'products':products,'category_name':name})
  else:
    messages.warning(request,'NOs such category found')
    return redirect('collections')
  
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')
    

def payment(request):
   return render (request,'shop/payment.html')    

def about(request):
   return render (request,'shop/about.html')

def contact(request):
   return render (request,'shop/contact.html')

