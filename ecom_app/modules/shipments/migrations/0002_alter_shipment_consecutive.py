# Generated by Django 3.2.9 on 2021-12-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='consecutive',
            field=models.IntegerField(null=True, verbose_name='Consecutivo'),
        ),
    ]
