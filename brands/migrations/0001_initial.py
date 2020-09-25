# Generated by Django 3.1.1 on 2020-09-18 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=120)),
                ('brand_description', models.TextField(null=True)),
                ('brand_logo', models.ImageField(upload_to='img/logo/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_description', models.TextField(max_length=850, null=True)),
                ('product_image', models.ImageField(upload_to='img/product/')),
                ('product_brand', models.ManyToManyField(related_name='brands', to='brands.Brands')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='brands',
            name='brand_product_category',
            field=models.ManyToManyField(related_name='brand_categories', to='brands.ProductCategory'),
        ),
    ]