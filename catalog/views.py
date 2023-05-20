from django.shortcuts import render
from .models import Producto, Tienda,Categoria
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):

    return render(request,'registro.html')

def carrito(request):
    products = Producto.objects.all().order_by('price')[0:3]
    tiendas = Tienda.objects.all()
    cats = Categoria.objects.all()
    rows = [products[0:3]]
    total = 0
    for p in products:
        total += p.price
    context = {
        'stores':tiendas,
        'cats':cats,
        'products':products,
        'rows':rows,
        'total':total,
    }
    return render(request,'carrito.html',context=context)

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
    rows = [products[0:3],products[3:6],products[6:9]]
    context ={
        'products':products,
        'rows':rows,
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
    rows = [products[0:3],products[3:6],products[6:9]]
    context ={
        'products':products,
        'rows':rows,
        'store':store,
        'prev':id-1 if id>0 else id,
        'next':id+1,
        'order':order,
        'stores':tiendas,
        'cats':cats,
        'cat':cat,
    }
    return render(request,'storeproductos.html',context=context)

def filteredproducts(request,id,store,order,search):
    s =  Tienda.objects.get(name=store)
    tiendas = Tienda.objects.all()
    cats = Categoria.objects.all()
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
        'order':order,
        'stores':tiendas,
        'cats':cats,
    }
    return render(request,'storeproductos.html',context=context)


