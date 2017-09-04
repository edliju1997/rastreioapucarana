from django.db import models

class PedidoAdmin(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
)

class Pedido(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', help_text='(Somente números)', max_length=11)
    telefone = models.CharField('telefone', help_text='(Somente números)', max_length=11)
    STATUS_CHOICES = (
        ('1', 'Pedido recebido'),
        ('2', 'Pedido em preparação'),
        ('3', 'Pedido saiu para entrega'),
    )
    status = models.CharField('status do pedido', max_length=50, choices=STATUS_CHOICES)
    observacoes = models.TextField('observações', blank=True)
    created_at = models.DateTimeField('pedido realizado em', auto_now_add=True)

    objects = PedidoAdmin()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'