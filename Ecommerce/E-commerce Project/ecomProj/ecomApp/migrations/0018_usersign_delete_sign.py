# Generated by Django 5.0 on 2024-04-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0017_rename_signn_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usersign',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='SIGN',
        ),
    ]