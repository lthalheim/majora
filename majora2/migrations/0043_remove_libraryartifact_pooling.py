# Generated by Django 2.2.10 on 2020-03-31 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0042_auto_20200331_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraryartifact',
            name='pooling',
        ),
    ]
