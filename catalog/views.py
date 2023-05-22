from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Producto, Tienda,Categoria,Usuario,Carrito
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Check if username or email already exist
            if Usuario.objects.filter(username=username).exists() or Usuario.objects.filter(mail=email).exists():
                form.add_error('username', "Username or email already exists.")
                # Render the template with the form and error message
                return render(request, 'registro.html', {'form': form})
                
            # Create a new instance of the Usuario model
            user = Usuario(username=username, mail=email, password=password)
            user.save()

            # Create an instance of the Carrito model for the current user
            carrito = Carrito(usuario=user)
            carrito.save()

            # Additional steps like sending a confirmation email, logging in the user, etc.
            # ...

            return redirect('login')  # Replace 'index' with your desired URL name
    else:
        form = RegisterForm()

    return render(request, 'registro.html', {'form': form})

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


