# Generated by Django 3.1.1 on 2020-09-22 14:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_remove_singlepage_full_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlepage',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
