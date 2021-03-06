# Generated by Django 2.2.10 on 2020-03-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0010_auto_20200318_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biosourcesamplingprocess',
            old_name='collection_org',
            new_name='submission_org',
        ),
        migrations.RenameField(
            model_name='biosourcesamplingprocess',
            old_name='collection_by',
            new_name='submitted_by',
        ),
        migrations.AddField(
            model_name='biosamplesource',
            name='source_age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='biosourcesamplingprocess',
            name='private_collection_location_adm2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
