# Generated by Django 3.2.9 on 2021-12-04 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('category', models.CharField(max_length=20, verbose_name='Categoria')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='Descripcion')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
