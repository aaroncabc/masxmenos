from django.db import models
import uuid 
# Create your models here.
class Tienda(models.Model):
    name = models.CharField(max_length=20) 
    def __str__(self) -> str:
        return self.name


class Producto(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    store = models.ForeignKey('Tienda',on_delete=models.SET_NULL, null=True)
    cat = models.ForeignKey('Categoria',on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.name},{self.price},[{self.store}{self.cat}]'
    
    
class Categoria(models.Model):
    name  = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Carrito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField('Producto')

    def display_items(self):
        return ', '.join(items.name for items in self.items.all()[:3])
    display_items.short_description = 'Poducto'


class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    username = models.CharField(max_length=20)
    mail = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.name},{self.mail}'