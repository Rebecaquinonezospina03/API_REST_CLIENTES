# Generated by Django 4.2.7 on 2023-11-22 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_numero_de_pedido_pedido_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clientes', to='clientes.producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('Elije', 'Elije'), ('camisa', 'Camisa'), ('pantalon', 'Pantalón'), ('vestido', 'Vestido')], default='Elije', max_length=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]