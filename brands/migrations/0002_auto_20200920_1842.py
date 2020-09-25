# Generated by Django 3.1.1 on 2020-09-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='brand_index',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brands',
            name='show_brand',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_index',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='show_product',
            field=models.BooleanField(default=True),
        ),
    ]
