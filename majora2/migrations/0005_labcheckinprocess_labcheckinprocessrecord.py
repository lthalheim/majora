# Generated by Django 2.1.4 on 2019-08-19 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0004_biosampleartifact_biosamplesource'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabCheckinProcess',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('originating_site', models.CharField(max_length=512)),
                ('originating_user', models.CharField(max_length=64)),
                ('originating_mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='LabCheckinProcessRecord',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
                ('damaged', models.BooleanField(default=False)),
                ('unexpected', models.BooleanField(default=False)),
                ('missing', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
    ]