from django.db import models
from base.models import Base
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from base.functions import send_email


class Shipment(Base):
    STATUS_OPTIONS = (
        ('Nuevo', 'Nuevo'),
        ('Despachado', 'Despachado'),
        ('Recibido', 'Recibido'),
    )
    consecutive = models.IntegerField('Consecutivo', null=True)
    status = models.CharField('Estado', blank=True, default='Nuevo',
                              null=True, choices=STATUS_OPTIONS, max_length=25)
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, null=True, blank=True)
    shipment_date = models.DateTimeField(
        'Fecha Despacho', null=True)
    received_date = models.DateTimeField(
        'Fecha Recibido', null=True)
    shipment_notification = models.BooleanField(default=False)
    received_notification = models.BooleanField(default=False)

    def __str__(self):
        return f"SHP-{str(self.consecutive).zfill(7)}"


@receiver(pre_save, sender=Shipment, dispatch_uid="update_before_count")
def update_before(sender, instance, **kwargs):
    if not instance.consecutive:
        consecutive = instance.__class__.objects.all().count() + 1
        instance.consecutive = consecutive
        instance.name = f"SHP-{str(consecutive).zfill(7)}"

    if not instance.shipment_date and instance.status == 'Despachado':
        instance.shipment_date = timezone.now()

    if not instance.received_date and instance.status == 'Recibido':
        instance.received_date = timezone.now()

    return True


@receiver(post_save, sender=Shipment, dispatch_uid="update_after_count")
def update_after(sender, instance, **kwargs):
    update_dict = {}
    if instance.status == 'Despachado' and not instance.shipment_notification:
        subject = f'Su pedido {instance.order} ha sido {instance.status}'
        body = f'Su pedido {instance.order} ha sido {instance.status} el {instance.shipment_date.strftime("%d/%m/%Y")}'
        update_dict['shipment_notification'] = True

    if instance.status == 'Recibido' and not instance.received_notification:
        subject = f'Su pedido {instance.order} ha sido {instance.status}'
        body = f'Su pedido {instance.order} ha sido {instance.status} el {instance.received_date.strftime("%d/%m/%Y")}'
        update_dict['received_notification'] = True

    if update_dict:
        instance.__class__.objects.filter(id=instance.id).update(**update_dict)
        send_email(subject=subject, body=body,
                   rcpt=[instance.created_by.email])

    return True