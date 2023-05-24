from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/<int:id>/<str:order>/<str:cat>', views.productosn, name='productosn'),
    path('productos/<int:id>/<str:store>/<str:order>/<str:cat>', views.storeproductosn, name='storeproductosn'),
    path('login',views.login,name='login'),
    path('register',views.register ,name='register'),
    path('carrito',views.carrito,name='carrito'),
    path('productos/<int:id>/<str:store>/<str:order>/<str:search>',views.filteredproducts,name=''),
    path('logout',views.logout,name='logout'),
    path('add/<str:product>',views.addProductToCart,name='add'),
    path('remoce/<int:product>',views.removeProductFromCart,name='remove'),
    path('filtercart/<str:parameter>/<str:value>',views.filtercart,name='filtercart'),
]

