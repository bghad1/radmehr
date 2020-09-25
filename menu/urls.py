from django.urls import path
from . import views

app_name = 'menus'

urlpatterns = [
    path('<slug>', views.menu_view, name="menu_view"),
]
