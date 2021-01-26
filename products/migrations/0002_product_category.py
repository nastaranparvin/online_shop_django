# Generated by Django 3.1.4 on 2021-01-19 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category'),
            preserve_default=False,
        ),
    ]
