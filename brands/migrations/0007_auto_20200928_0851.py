# Generated by Django 3.1.1 on 2020-09-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0006_auto_20200928_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=250, null=True, verbose_name='آدرس لینک'),
        ),
    ]
