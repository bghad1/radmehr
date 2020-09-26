# Generated by Django 3.1.1 on 2020-09-26 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20200922_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name': 'برند', 'verbose_name_plural': 'برندها'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'دسته بندی محصول', 'verbose_name_plural': 'دسته بندی محصولات'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_description',
            field=models.TextField(null=True, verbose_name='توضیح برند'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_index',
            field=models.IntegerField(verbose_name='ردیف نمایش'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_logo',
            field=models.ImageField(upload_to='img/logo/', verbose_name='تصویر لوگو'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_name',
            field=models.CharField(max_length=120, verbose_name='نام برند'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_product_category',
            field=models.ManyToManyField(related_name='brand_categories', to='brands.ProductCategory', verbose_name='دسته بندی محصولات'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='show_brand',
            field=models.BooleanField(default=True, verbose_name='نمایش'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.CharField(max_length=30, verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_brand',
            field=models.ManyToManyField(related_name='brands', to='brands.Brands', verbose_name='نام برند'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.productcategory', verbose_name='دسته بندی محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_description',
            field=models.TextField(max_length=850, null=True, verbose_name='توضیح کامل محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='img/product/', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_index',
            field=models.IntegerField(verbose_name='ترتیب نمایش'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=150, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='show_product',
            field=models.BooleanField(default=True, verbose_name='نمایش'),
        ),
    ]