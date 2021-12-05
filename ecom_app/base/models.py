import uuid
from django.db import models
from django.conf import settings


class Base(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nombre', max_length=255, blank=True, null=True)
    creation_date = models.DateTimeField('Fecha Creacion', auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):

        return f"{self.name if self.name else ''}"
