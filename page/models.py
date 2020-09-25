from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField


# from django import forms
# from tinymce.widgets import TinyMCE


class SinglePage(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان برگه')
    slug = models.SlugField(max_length=250, verbose_name='آدرس لینک')
    # body = models.TextField()
    body = HTMLField(verbose_name='متن کامل')
    # text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 50, 'class': 'form-control'}))
    # content = HTMLField()
    head_img = models.ImageField(upload_to='img/page/', verbose_name='تصویر اصلی')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='نوشته شده در')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='آخرین تغییر در')
    show_page = models.BooleanField(default=True, verbose_name='نمایش')
    page_index = models.IntegerField(verbose_name='ترتیب نمایش')

    # full_body = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برگه'
        verbose_name_plural = "برگه ها"


def get_absolute_url(self):
    return reverse('pages:page_detail', args=[str(self.id)])
    # return reverse('pages:page_detail', kwargs={'slug': self.slug, 'id': self.id})
