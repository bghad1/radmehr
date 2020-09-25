# Generated by Django 3.1.1 on 2020-09-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200923_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('seminar', 'سمینار'), ('exhibition', 'نمایشگاه')], default='seminar', max_length=15),
        ),
    ]