# from django.shortcuts import get_object_or_404
from menu.models import Menu  # MenuItem
from django.shortcuts import render


def menu_view(request, slug):
    menu_element = Menu.objects.get(slug=slug)
    context = {
        'show_menu_element': menu_element
    }
    # return render(request, 'brand_view.html', context)
    return render(request, 'menu.html', context)


# def menu_detail(request):
#     brand = Brands.objects.all()
#     context = {
#         'brand_in_menu': brand
#     }
#     # return render(request, 'brand_view.html', context)
#     return render(request, 'menu-brand.html', context)
#
#
#
# # def menu_detail(request, slug):
# #     parent_menu = get_object_or_404(Menu, slug=slug)
# #     # the_menu = Menu.objects.get(slug=slug)
# #     # menu_item = get_object_or_404(MenuItem, link_url)
# #     menu_item = MenuItem.objects.filter(menu=parent_menu)
# #     context = {
# #         'menu': parent_menu,
# #         'menu-item': menu_item
# #     }
# #     return render(request, 'menu-brand.html', context)
#
