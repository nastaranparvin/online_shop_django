# Generated by Django 3.1.4 on 2021-01-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210120_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('1', 'Order is begin registered'), ('2', 'Delivered to the sales unit'), ('3', 'Loading'), ('4', 'Sending'), ('5', 'Cleared')], default='1', max_length=1, verbose_name='Order status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number_order',
            field=models.CharField(default='WBN-1611138755', max_length=20, verbose_name='Number_order'),
        ),
    ]