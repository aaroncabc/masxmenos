from django.shortcuts import render
from .models import Producto, Tienda,Categoria
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def productosn(request,id,order,cat):

    i=id*9
    n = i+9  # number of objects to retrieve
    tiendas = Tienda.objects.all()
    cats = Categoria.objects.all()
    if cat !='all' : 
        if(order=='asc'):
            products = Producto.objects.all().filter(cat=cat).order_by('price')[i:n]
        else:
            products = Producto.objects.all().filter(cat=cat).order_by('-price')[i:n]
    else:
        if(order=='asc'):
            products = Producto.objects.all().order_by('price')[i:n]
        else:
            products = Producto.objects.all().order_by('-price')[i:n]
    context ={
        'products':products,
        'prev':id-1 if id>0 else id,
        'next':id+1,
        'order':order,
        'stores':tiendas,
        'cats':cats,
        'cat':cat,
    }
    return render(request,'productos.html',context=context)


def storeproductosn(request,id,store,order,cat):
    s =  Tienda.objects.get(name=store)
    tiendas = Tienda.objects.all()
    cats = Categoria.objects.all()
    i=id*9
    n = i+9  # number of objects to retrieve
    if cat !='all':
        if(order=='asc'):
            products = Producto.objects.filter(store=s).filter(cat=cat).order_by('price')[i:n]
        else:
            products = Producto.objects.filter(store=s).filter(cat=cat).order_by('-price')[i:n]
    else:    
        if(order=='asc'):
            products = Producto.objects.filter(store=s).order_by('price')[i:n]
        else:
            products = Producto.objects.filter(store=s).order_by('-price')[i:n]
    context ={
        'products':products,
        'store':store,
        'prev':id-1 if id>0 else id,
        'next':id+1,
        'order':order,
        'stores':tiendas,
        'cats':cats,
        'cat':cat,
    }
    return render(request,'storeproductos.html',context=context)

