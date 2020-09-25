from django.urls import path
from . import views

app_name = 'contact_us'

urlpatterns = [
    path('', views.home_contact_us, name='home')
]
