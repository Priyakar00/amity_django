# Generated by Django 5.0 on 2024-04-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0009_order_delete_orders_delete_orderupdate'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='sign',
        #     name='id',
        # ),
        migrations.AlterField(
            model_name='sign',
            name='email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
