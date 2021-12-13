from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_ID=ca_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.qnty)
            count+=i.qnty
    except ObjectDoesNotExist:
        pass
    return render(request,'card.html',{'ci':ct_items,'t':tot,'c':count})

def ca_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prdt=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_ID=ca_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_ID=ca_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prdt,cart=ct)
        if c_items.qnty < c_items.prodt.stock:
            c_items.qnty+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prdt,qnty=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_ID=ca_id(request))
    prd=get_object_or_404(product,id=product_id)
    ct_items=items.objects.get(prodt=prd,cart=ct)
    if ct_items.qnty>1:
        ct_items.qnty-=1
        ct_items.save()
    else:
        ct_items.delete()
    return redirect('cartDetails')


def cart_delete(request,product_id):
    ct=cartlist.objects.get(cart_ID=ca_id(request))
    prd=get_object_or_404(product,id=product_id)
    ct_items=items.objects.get(prodt=prd,cart=ct)
    ct_items.delete()
    return redirect('cartDetails')
    
