# Generated by Django 3.1.1 on 2020-09-24 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventtype'),
        ),
    ]
