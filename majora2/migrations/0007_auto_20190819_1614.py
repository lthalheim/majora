# Generated by Django 2.1.4 on 2019-08-19 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0006_auto_20190819_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majoraartifactprocessrecord',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='records', to='majora2.MajoraArtifactProcess'),
        ),
    ]