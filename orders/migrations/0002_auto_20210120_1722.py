# Generated by Django 3.1.4 on 2021-01-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number_order',
            field=models.CharField(default='FPJ-1611138148', max_length=20, verbose_name='Number_order'),
        ),
    ]
