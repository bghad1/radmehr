# Generated by Django 3.1.1 on 2020-09-26 13:34

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_auto_20200922_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='singlepage',
            options={'verbose_name': 'برگه', 'verbose_name_plural': 'برگه ها'},
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='متن کامل'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='نوشته شده در'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='head_img',
            field=models.ImageField(upload_to='img/page/', verbose_name='تصویر اصلی'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='آخرین تغییر در'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='page_index',
            field=models.IntegerField(verbose_name='ترتیب نمایش'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='show_page',
            field=models.BooleanField(default=True, verbose_name='نمایش'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='slug',
            field=models.SlugField(max_length=250, verbose_name='آدرس لینک'),
        ),
        migrations.AlterField(
            model_name='singlepage',
            name='title',
            field=models.CharField(max_length=255, verbose_name='عنوان برگه'),
        ),
    ]