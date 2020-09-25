from django.contrib import admin
from brands.models import Brands, Products, ProductCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "show_brand", "brand_index")
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "show_product", "product_index")
    list_filter = ("product_category",)
    pass


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    pass


admin.site.register(Brands, PostAdmin)
admin.site.register(Products, CategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

