# Requeridos
from django.contrib import admin
# Si mismo
from compras.models import Comprobante
from compras.models import Elemento

class ElementoInline(admin.TabularInline):
	readonly_fields = ['unidad', 'precio_unitario']
	fields = ('articulo', 'cantidad', 'unidad', 'detalle', 'precio_unitario', 'precio')
	model = Elemento
	extra = 3

	def precio_unitario(self,obj):
		precio = obj.precio/obj.cantidad
		return precio

	def unidad(self,obj):
		return obj.producto.unidad

class ComprobanteAdmin(admin.ModelAdmin):
	inlines = [ElementoInline]
	list_display = ('fecha', 'tipo', 'serie', 'numero', 'cliente', 'elementos','monto')

	def elementos(self,obj):
		return Elemento.objects.filter(articulo=obj.id).count()

	def monto(self,obj):
		total = 0
		Elementos = Elemento.objects.filter(articulo=obj.id)
		for item in Elementos:
			total = total + item.precio
		return total

admin.site.register(Comprobante, ComprobanteAdmin)