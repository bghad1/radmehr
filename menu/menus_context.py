from menu.models import Menu, MenuItem


def show_menu(context):
    main_menu = Menu.objects.filter(show_menu=True)
    main_menu_item = MenuItem.objects.filter(show_menu_item=True)
    # mycontext = {
    #     'main_menu': main_menu,
    #     'main_menu_item': main_menu_item,
    # }
    # return mycontext
    return {'main_menu': main_menu, 'main_menu_item': main_menu_item}
