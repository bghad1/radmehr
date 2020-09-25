# Generated by Django 3.1.1 on 2020-09-24 08:50

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20200924_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='events',
            field=models.ForeignKey(on_delete=models.SET(event.models.get_deleted_event_type), to='event.eventtype'),
        ),
    ]