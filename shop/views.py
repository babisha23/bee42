from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prdt=None
    if c_slug!=None:
        c_page=get_object_or_404(cata,slug=c_slug)
        prdt=product.objects.filter(catagery=c_page,available=True)
    else:
        prdt=product.objects.all().filter(available=True)
    cat=cata.objects.all()
    paginator=Paginator(prdt,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'pdt':prdt,'cat':cat,'pg':pro})


def pdtdetails(request,c_slug,product_slug):
    try:
        pd=product.objects.get(catagery__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'items.html',{'pdt':pd})

def search(request):
    pd=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        pd=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'pdt':pd})