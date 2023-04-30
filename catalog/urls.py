from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/<int:id>/<str:order>', views.productosn, name='productosn'),
    path('productos/<int:id>/<str:store>/<str:order>', views.storeproductosn, name='storeproductosn'),
]

