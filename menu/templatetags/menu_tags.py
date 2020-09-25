from django import template
from ..models import Menu  # , MenuItem
# from brands.models import Brands


register = template.Library()


@register.inclusion_tag('menu.html')
def show_menu_elements():
    latest_menus = Menu.objects.filter(show_menu=True).order_by('menu_index')
    context = {
        'latest_menu_elements': latest_menus
    }
    return context
#
#
# # @register.inclusion_tag('menu-brand.html')
# # def show_latest_menu(count=5):
# #     # latest_menus = Menu.objects.all()[:count]
# #     latest_menus = Menu.objects.order_by('-name')[:count]
# #     latest_menu_items = MenuItem.objects.filter(menu=latest_menus)
# #     context = {
# #         'latest_menus': latest_menus,
# #         'latest_menu_items': latest_menu_items
# #     }
# #     return context