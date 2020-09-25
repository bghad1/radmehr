from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from homepage.views import homepage
from django.conf.urls.static import static
from django.conf import settings


sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('brand/', include('brands.urls', namespace='brands')),
    path(r'brand/', include('brands.urls', namespace='brands')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('homepage.urls', namespace='homepage')),
    path('aboutus/', include('about_us.urls', namespace='about_us')),
    path('contactus/', include('contact_us.urls', namespace='contact_us')),
    path('page/', include('page.urls', namespace='pages')),
    path('event/', include('event.urls', namespace='events')),
    path('tinymce/', include('tinymce.urls'))
    # path('<slug>', include('page.urls', namespace='pages')),
    # path('', include('homepage.urls', namespace='home')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #      name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


