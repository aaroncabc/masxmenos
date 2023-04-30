from django.shortcuts import render
from .models import Producto, Tienda
# Create your views here.
def index(request):
    return render(request,'index.html')

def productosn(request,id,order):

    i=id*9
    n = i+9  # number of objects to retrieve
    if(order=='asc'):
        products = Producto.objects.all().order_by('price')[i:n]
    else:
        products = Producto.objects.all().order_by('-price')[i:n]
    context ={
        'products':products,
        'prev':id-1 if id>0 else id,
        'next':id+1,
        'order':order,
    }
    return render(request,'productos.html',context=context)


def storeproductosn(request,id,store,order):
    s =  Tienda.objects.get(name=store)
    i=id*9
    n = i+9  # number of objects to retrieve
    if(order=='asc'):
        products = Producto.objects.filter(store=s).order_by('price')[i:n]
    else:
        products = Producto.objects.filter(store=s).order_by('-price')[i:n]
    context ={
        'products':products,
        'store':store,
        'prev':id-1 if id>0 else id,
        'next':id+1,
        'order':order
    }
    return render(request,'storeproductos.html',context=context)

