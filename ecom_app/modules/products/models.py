from django.db import models
from base.models import Base


class Product(Base):
    price = models.FloatField("Precio")
    category = models.CharField("Categoria", max_length=20)
    description = models.CharField(
        "Descripcion", max_length=200, null=True, blank=False)
