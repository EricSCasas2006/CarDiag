# Generated by Django 4.2.5 on 2023-12-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='modo_pago',
            field=models.CharField(choices=[('nequi', 'Nequi'), ('tarjeta_credito', 'Tarjeta de Crédito'), ('tarjeta_debito', 'Tarjeta de Débito'), ('efectivo', 'Efectivo')], max_length=20),
        ),
    ]
