# Generated by Django 4.0.2 on 2022-02-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productmodel_real_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='shop.ColorModel', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='shop.SizeModel', verbose_name='size'),
        ),
    ]