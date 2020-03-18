# Generated by Django 2.2.10 on 2020-03-18 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0002_institution'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Institution',
            new_name='Institute',
        ),
        migrations.AddField(
            model_name='profile',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='majora2.Institute'),
        ),
    ]