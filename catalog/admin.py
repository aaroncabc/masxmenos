from django.contrib import admin
from django.db.models import F

class PriceSortFilter(admin.SimpleListFilter):
    title = 'Price Sort'
    parameter_name = 'price_sort'

    def lookups(self, request, model_admin):
        return (
            ('asc', 'Ascending'),
            ('desc', 'Descending'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'asc':
            return queryset.order_by(F('price').asc(nulls_last=True))
        elif self.value() == 'desc':
            return queryset.order_by(F('price').desc(nulls_last=True))
        else:
            return queryset
        

# Register your models here.
from .models import Producto,Tienda,Carrito,Categoria,Usuario
# Register your models here.

#admin.site.register(Productos)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store','cat')
    list_filter = ('store',PriceSortFilter,'cat')


admin.site.register(Tienda)


#admin.site.register(Carritos)
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario','display_items')


admin.site.register(Categoria)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','mail')