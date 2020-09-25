from django.contrib import admin
from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    # path('', views.home_view, name='home'),
    path('', views.brand_view, name='brand'),
    path('contact/', views.contact, name='contact'),
    path('<brand_name>/', views.brand_detail_View, name="brand_detail"),
]
