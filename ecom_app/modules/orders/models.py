from django.db import models
from base.models import Base


class Order(Base):
    STATUS_OPTIONS = (
        ('Nuevo', 'Nuevo'),
        ('Pagado', 'Pagado'),
        ('Enviado', 'Enviado'),
    )
    id = models.AutoField(primary_key=True)
    status = models.CharField('Estado', blank=True, default='Nuevo',
                              null=True, choices=STATUS_OPTIONS, max_length=25)

    def __str__(self):
        return f"OR-{str(self.id).zfill(7)}"


class OrderMvto(Base):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.FloatField("Valor", default=0)
    cant = models.FloatField("Cantidad", default=1, blank=True)

    REQUIRED_FIELDS = ['product', 'cant']

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"OR-MV-{str(self.id).zfill(7)}"
