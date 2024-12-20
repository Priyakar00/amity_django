# Generated by Django 5.0 on 2023-12-20 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imag', models.ImageField(null=True, upload_to='product_image/')),
                ('active', models.BooleanField(default=True)),
                ('single_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomApp.product')),
            ],
        ),
    ]
