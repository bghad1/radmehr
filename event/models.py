from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from extensions.utils import shamsi_converter


class EventType(models.Model):
    # EVENT_CHOICES = (
    #     ('seminar', 'سمینار'),
    #     ('exhibition', 'نمایشگاه'),
    # )
    # event_type = models.CharField(max_length=15,
    #                               choices=EVENT_CHOICES,
    #                               default='seminar')
    name = models.CharField(max_length=20, verbose_name="نوع رویداد")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نوع رویداد"
        verbose_name_plural = "انواع رویداد"


def get_deleted_event_type():
    return EventType.objects.get(name='رویداد دسته بندی نشده')


class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'پیش نویس'),
        ('published', 'منتشر شده'),
    )
    EVENT_CHOICES = (
        ('seminar', 'سمینار'),
        ('exhibition', 'نمایشگاه'),
    )
    title = models.CharField(max_length=255, verbose_name='عنوان رویداد')
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish', allow_unicode=True,
                            verbose_name='آدرس لینک', unique=True)
    body = HTMLField(verbose_name='متن کامل')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='نوشته شده در')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='آخرین تغییر در')
    events = models.ForeignKey(EventType, on_delete=models.SET(get_deleted_event_type),
                               verbose_name='ارتباط با کدام رویداد')
    event_type = models.CharField(max_length=15,
                                  choices=EVENT_CHOICES,
                                  default='seminar',
                                  verbose_name='نوع رویداد')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',
                              verbose_name='وضعیت نمایش')
    event_index = models.IntegerField(verbose_name='ترتیب نمایش')

    class Meta:
        ordering = ('-publish',)
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"

    def __str__(self):
        return self.title

    def shamsidate(self):
        return shamsi_converter(self.publish)
    shamsidate.short_description = "زمان انتشار"
