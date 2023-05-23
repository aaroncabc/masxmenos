from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Producto, Tienda,Categoria,Usuario,Carrito
# Create your views here.
def index(request):
    user_id = request.session['user_id'] if 'user_id' in request.session else None
    context = {
        'user_id': user_id,
    }
    return render(request,'index.html',context=context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Check if the username and password combination exist in the database
        if Usuario.objects.filter(username=username, password=password).exists():
            # Get the user object
            user = Usuario.objects.get(username=username, password=password)
            # Create a new session key which is used to identify the user
            request.session['user_id'] = user.username
            # Redirect to the index page
            return redirect('index')
        else:
            # Render the template with an error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
            
    return render(request,'login.html')

def logout(request):
    # Delete the user session key
    del request.session['user_id']
    # Redirect to the index page
    return redirect('index')

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
    user_id = request.session['user_id']
    products = Carrito.objects.get(usuario__username=user_id).items.all()
    tiendas = Tienda.objects.all()
    cats = Categoria.objects.all()
    rows = [products[i:i + 3] for i in range(0, len(products), 3)]
    total = 0
    for p in products:
        total += p.price
    context = {
        'stores':tiendas,
        'cats':cats,
        'products':products,
        'rows':rows,
        'total':total,
        'user_id':user_id,
    }
    return render(request,'carrito.html',context=context)

def productosn(request,id,order,cat):
    user_id = request.session['user_id']
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
        'user_id':user_id,
    }
    return render(request,'productos.html',context=context)


def storeproductosn(request,id,store,order,cat):
    user_id = request.session['user_id']
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
        'user_id':user_id,
    }
    return render(request,'storeproductos.html',context=context)

def filteredproducts(request,id,store,order,search):
    user_id = request.session['user_id']
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
        'search':search,
        'user_id':user_id,
    }
    return render(request,'storeproductos.html',context=context)


