# Generated by Django 3.1.1 on 2020-09-22 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_singlepage_full_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlepage',
            name='full_body',
        ),
    ]
