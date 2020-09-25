from django.urls import path
from . import views
from django.urls import re_path

app_name = 'events'

urlpatterns = [
    path('seminar/', views.seminar_view, name="seminar_view"),
    path('exhibition/', views.exhibition_view, name="exhibition_view"),
    re_path(r'seminar/(?P<slug>[-\w]+)/', views.seminar_detail, name="seminar_detail"),
    re_path(r'exhibition/(?P<slug>[-\w]+)/$', views.exhibition_detail, name="exhibition_detail"),
    # path('seminar/<slug>', views.seminar_detail, name="seminar_detail"),
    # path('exhibition/<slug>', views.exhibition_detail, name="exhibition_detail"),
    # path('', views.PostListView.as_view(), name='post_list'),
    # path('<str:title>', views.blog_detail, name="blog_detail"),
]
