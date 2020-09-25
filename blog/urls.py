from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name="blog_view"),
    path('<slug>', views.blog_detail, name="blog_detail"),
    # path('', views.PostListView.as_view(), name='post_list'),
    # path('<str:title>', views.blog_detail, name="blog_detail"),
    path('category/<category>', views.blog_category, name="blog_category"),
]
