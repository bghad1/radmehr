from django.shortcuts import render
from brands.models import Brands, Products


# Create your views here.
# def home_view(request):
#     return render(request, 'index.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def brand_view(request):
    brand = Brands.objects.all()
    context = {
        'brand': brand
    }
    # return render(request, 'brand_view.html', context)
    return render(request, 'brand-sanje.html', context)


def brand_detail_View(request, brand_slug):
    # show_brand = Brands.objects.filter(show_brand=True)
    brand_detail = Brands.objects.get(brand_slug=brand_slug)
    # products = Products.objects.get(product_brand=brand_name)
    products = Products.objects.filter(product_brand=brand_detail)
    # brand_category = Brands.objects.get(brand_product_category=brand_name)
    # products_category = Products.objects.filter(product_brand=brand_detail, prodcut_category=product_category)
    # products = Products.objects.select_related('product_brand').get(product_brand=brand_name)
    context = {
        'brand_detail': brand_detail,
        'products': products,
        # 'brand_category': brand_category
    }
    # return render(request, 'brand_detail.html', context)
    return render(request, 'brand-page.html', context)


# def products_view(request, product_name):
#     products = Products.objects.get(product_name=product_name)
#     context = {
#         'products': products
#     }
#     return render(request, 'brand-page.html', context)

# def brand_detail_View(request, bk, brand_name):
#     brand_detail = Brands.objects.get(pk=bk)
#     context = {
#         'brand_detail': brand_detail
#     }
#     # return render(request, 'brand_detail.html', context)
#     return render(request, 'brand-page.html', context)
#
#
