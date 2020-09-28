from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'brands'

urlpatterns = [
    # path('', views.home_view, name='home'),
    path('', views.brand_view, name='brand'),
    path('contact/', views.contact, name='contact'),
    path('<slug:brand_slug>/', views.brand_detail_View, name="brand_detail"),
    # re_path(r'(?P<slug>[-\w]+)/$', views.brand_detail_View, name="brand_detail"),
]
