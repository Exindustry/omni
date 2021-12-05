from django.db import models
from base.models import Base


class Payment(Base):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField('Amount', blank=True, null=True, default=0)
    orders =  models.ManyToManyField('orders.Order', through='payments.PaymentMvto')

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return f"PM-{str(self.id).zfill(5)}"


class PaymentMvto(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
            "orders.Order", on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey("payments.Payment", on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField('Amount', blank=True, null=True)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return f"PM-MV-{str(self.id).zfill(5)}"
