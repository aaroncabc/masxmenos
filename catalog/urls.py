from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/<int:id>/<str:order>/<str:cat>', views.productosn, name='productosn'),
    path('productos/<int:id>/<str:store>/<str:order>/<str:cat>', views.storeproductosn, name='storeproductosn'),
    path('login',views.login,name='login'),
    path('register',views.register ,name='register')

]

