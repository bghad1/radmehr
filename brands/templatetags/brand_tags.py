from django import template
from ..models import Brands

register = template.Library()


@register.inclusion_tag('menu-brand.html')
def show_brands_in_menu():
    # latest_menus = Menu.objects.all()[:count]
    # latest_brands_menu = Brands.objects.order_by('-name')[:count]
    latest_brands_menu = Brands.objects.filter(show_brand=True).order_by('brand_index')
    # latest_brands_menu = Brands.objects.order_by('-brand_name')  #[:count]
    # latest_menu_items = MenuItem.objects.filter(menu=latest_menus)
    # context = {
    #     'latest_brands_menu': latest_brands_menu,
    #     # 'latest_menu_items': latest_menu_items
    # }
    return {'latest_brands_menu': latest_brands_menu}

