from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام منو')
    slug = models.SlugField(verbose_name='آدرس لینک')
    base_url = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    show_menu = models.BooleanField(default=True, verbose_name='نمایش')
    menu_index = models.IntegerField(verbose_name='ترتیب نمایش')

    class Meta:
        verbose_name = "منو"
        verbose_name_plural = "منوها"

    def __str__(self):
        return self.name

    def save(self):
        """
        Re-order all items at from 10 upwards, at intervals of 10.
        This makes it easy to insert new items in the middle of
        existing items without having to manually shuffle
        them all around.
        """
        super(Menu, self).save()

        current = 10
        for item in MenuItem.objects.filter(menu=self).order_by('order'):
            item.order = current
            item.save()
            current += 10


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='عضوی از منوی')
    order = models.IntegerField(verbose_name='ردیف')
    link_url = models.CharField(max_length=100, help_text='URL or URI to the content, eg /about/ or http://foo.com/')
    title = models.CharField(max_length=100, verbose_name='عنوان آیتم منو')
    show_menu_item = models.BooleanField(default=False, verbose_name='ترتیب نمایش')
    # login_required = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "گزینه منو"
        verbose_name_plural = "گزینه های منو"

    def __str__(self):
        return "%s %s. %s" % (self.menu.slug, self.order, self.title)
