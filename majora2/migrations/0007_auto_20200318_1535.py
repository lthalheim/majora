# Generated by Django 2.2.10 on 2020-03-18 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0006_auto_20200318_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biosourcesamplingprocess',
            old_name='collection_location_adm0',
            new_name='collection_location_adm1',
        ),
    ]
