from django.db import models


# Create your models here.
class Brands(models.Model):
    brand_name = models.CharField(max_length=120, verbose_name='نام برند')
    brand_description = models.TextField(null=True, verbose_name='توضیح برند')
    brand_logo = models.ImageField(upload_to='img/logo/', verbose_name='تصویر لوگو')
    brand_product_category = models.ManyToManyField('ProductCategory',
                                                    related_name='brand_categories',
                                                    verbose_name='دسته بندی محصولات')
    show_brand = models.BooleanField(default=True, verbose_name='نمایش')
    brand_index = models.IntegerField(verbose_name='ردیف نمایش')
    # brand_logo = models.FilePathField(path="/img/logo")

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=30, verbose_name='دسته بندی')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "دسته بندی محصول"
        verbose_name_plural = "دسته بندی محصولات"


class Products(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='نام محصول')
    product_brand = models.ManyToManyField('Brands', related_name='brands', verbose_name='نام برند')
    # product_category = models.ManyToManyField('ProductCategory', related_name='products_categories')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                         verbose_name='دسته بندی محصول')
    # product_brand = models.CharField(max_length=100, null=True)
    product_description = models.TextField(max_length=850, null=True, verbose_name='توضیح کامل محصول')
    product_image = models.ImageField(upload_to='img/product/', verbose_name='تصویر محصول')
    show_product = models.BooleanField(default=True, verbose_name='نمایش')
    product_index = models.IntegerField(verbose_name='ترتیب نمایش')
    # product_image = models.FilePathField(path="/img/product", null=True)

    def __str__(self):
        # return self.product_name, self.product_category, self.product_brand
        return f"{self.product_name}, {self.product_category}, {self.product_brand}"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
