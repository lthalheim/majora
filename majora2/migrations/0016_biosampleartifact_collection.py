# Generated by Django 2.2.10 on 2020-03-19 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0015_remove_biosampleartifact_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='biosampleartifact',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='biosamples', to='majora2.BiosourceSamplingProcessRecord'),
        ),
    ]
