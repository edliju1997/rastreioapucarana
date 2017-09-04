from django.contrib import admin

from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'status', 'cpf', 'telefone', 'created_at']

admin.site.register(Pedido, PedidoAdmin)