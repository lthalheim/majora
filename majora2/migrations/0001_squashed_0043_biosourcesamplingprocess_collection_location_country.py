# Generated by Django 2.1.4 on 2020-03-17 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('majora2', '0001_initial'), ('majora2', '0002_auto_20190818_1653'), ('majora2', '0003_digitalresourcegroup_current_name'), ('majora2', '0004_biosampleartifact_biosamplesource'), ('majora2', '0005_labcheckinprocess_labcheckinprocessrecord'), ('majora2', '0006_auto_20190819_1552'), ('majora2', '0007_auto_20190819_1614'), ('majora2', '0008_digitalresourcenode'), ('majora2', '0009_auto_20190819_1753'), ('majora2', '0010_digitalresourcecommand_digitalresourcecommandgroup_digitalresourcecommandpipelinegroup_digitalresour'), ('majora2', '0011_auto_20190819_1858'), ('majora2', '0012_auto_20190819_1902'), ('majora2', '0013_majoraartifactprocessgroup_root_group'), ('majora2', '0014_auto_20190820_1154'), ('majora2', '0015_majorametarecord'), ('majora2', '0016_majorametarecord_inheritable'), ('majora2', '0017_favourite'), ('majora2', '0018_auto_20190821_1333'), ('majora2', '0019_auto_20190823_1225'), ('majora2', '0020_majoraartifactgroup_processes'), ('majora2', '0021_auto_20190908_1019'), ('majora2', '0022_labcheckinprocessrecord_confusing'), ('majora2', '0023_auto_20191008_1724'), ('majora2', '0024_auto_20191008_1731'), ('majora2', '0025_majoraartifact_root_artifact'), ('majora2', '0026_auto_20191008_1754'), ('majora2', '0027_biosampleextractionprocess_biosampleextractionrecordprocess'), ('majora2', '0028_auto_20191009_1155'), ('majora2', '0029_auto_20191119_1842'), ('majora2', '0030_auto_20191119_1843'), ('majora2', '0031_digitalresourcecommandrecord_effect_status'), ('majora2', '0032_auto_20200110_1406'), ('majora2', '0033_auto_20200125_1654'), ('majora2', '0034_auto_20200125_1809'), ('majora2', '0035_auto_20200125_1821'), ('majora2', '0036_profile'), ('majora2', '0037_auto_20200317_1349'), ('majora2', '0038_auto_20200317_1411'), ('majora2', '0039_majoraartifactgroup_unique_name'), ('majora2', '0040_auto_20200317_1534'), ('majora2', '0041_majoraartifactprocess_group'), ('majora2', '0042_auto_20200317_1550'), ('majora2', '0043_biosourcesamplingprocess_collection_location_country')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MajoraArtifact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dice_name', models.CharField(blank=True, max_length=48, null=True)),
                ('meta_name', models.CharField(blank=True, max_length=48, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='MajoraArtifactGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dice_name', models.CharField(blank=True, max_length=48, null=True)),
                ('meta_name', models.CharField(blank=True, max_length=48, null=True)),
                ('physical', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcess',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('when', models.DateTimeField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcessGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='tagged_groups', to='majora2.MajoraArtifactProcessGroup')),
                ('parent_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='majora2.MajoraArtifactProcessGroup')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifactprocessgroup_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcessRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='DigitalResourceArtifact',
            fields=[
                ('majoraartifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifact')),
                ('current_name', models.CharField(max_length=512)),
                ('current_hash', models.CharField(max_length=64)),
                ('current_size', models.BigIntegerField(default=0)),
                ('ghost', models.BooleanField(default=False)),
                ('current_extension', models.CharField(default='', max_length=48)),
                ('current_kind', models.CharField(default='File', max_length=48)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifact',),
        ),
        migrations.CreateModel(
            name='DigitalResourceGroup',
            fields=[
                ('majoraartifactgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactGroup')),
                ('current_name', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactgroup',),
        ),
        migrations.CreateModel(
            name='TubeArtifact',
            fields=[
                ('majoraartifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifact')),
                ('container_x', models.PositiveSmallIntegerField()),
                ('container_y', models.PositiveSmallIntegerField()),
                ('storage_medium', models.CharField(max_length=24)),
                ('sample_form', models.CharField(blank=True, max_length=48, null=True)),
                ('tube_form', models.CharField(blank=True, max_length=48, null=True)),
                ('lid_label', models.CharField(blank=True, max_length=24, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifact',),
        ),
        migrations.CreateModel(
            name='TubeContainerGroup',
            fields=[
                ('majoraartifactgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactGroup')),
                ('container_type', models.CharField(max_length=24)),
                ('contains_tubes', models.BooleanField(default=False)),
                ('dimension_x', models.PositiveSmallIntegerField()),
                ('dimension_y', models.PositiveSmallIntegerField()),
                ('parent_x', models.PositiveSmallIntegerField()),
                ('parent_y', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactgroup',),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessrecord',
            name='in_artifact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='before_process', to='majora2.MajoraArtifact'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessrecord',
            name='out_artifact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='after_process', to='majora2.MajoraArtifact'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessrecord',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifactprocessrecord_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessrecord',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majora2.MajoraArtifactProcess'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocess',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocess',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifactprocess_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocess',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='majoraartifactgroup',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='tagged_groups', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifactgroup',
            name='parent_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifactgroup',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifactgroup_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='majoraartifactgroup',
            name='root_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='descendants', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifact',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='tagged_artifacts', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifact',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifact_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='majoraartifact',
            name='primary_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='majora2.MajoraArtifactGroup'),
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcessRecordTest',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
                ('test_message', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcessTest',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('test_message', models.CharField(max_length=256)),
                ('test_user', models.CharField(max_length=24)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='BiosampleArtifact',
            fields=[
                ('majoraartifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifact')),
                ('sample_orig_id', models.CharField(max_length=24)),
                ('sample_type', models.CharField(max_length=24)),
                ('specimen_type', models.CharField(max_length=24)),
                ('sample_longitude', models.PositiveSmallIntegerField(default=0)),
                ('sample_batch', models.PositiveSmallIntegerField(default=0)),
                ('sample_batch_longitude', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifact',),
        ),
        migrations.CreateModel(
            name='BiosampleSource',
            fields=[
                ('majoraartifactgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactGroup')),
                ('source_type', models.CharField(max_length=24)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactgroup',),
        ),
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
                ('confusing', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.AlterField(
            model_name='majoraartifactprocessrecord',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='records', to='majora2.MajoraArtifactProcess'),
        ),
        migrations.CreateModel(
            name='DigitalResourceNode',
            fields=[
                ('majoraartifactgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactGroup')),
                ('node_name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactgroup',),
        ),
        migrations.CreateModel(
            name='DigitalResourceCommand',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('cmd_str', models.CharField(max_length=512)),
                ('return_code', models.SmallIntegerField(blank=True, null=True)),
                ('group_order', models.PositiveSmallIntegerField(default=0)),
                ('queued_at', models.DateTimeField()),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='DigitalResourceCommandGroup',
            fields=[
                ('majoraartifactprocessgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessGroup')),
                ('group_name', models.CharField(max_length=48)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessgroup',),
        ),
        migrations.CreateModel(
            name='DigitalResourceCommandPipelineGroup',
            fields=[
                ('majoraartifactprocessgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessGroup')),
                ('pipe_name', models.CharField(max_length=48)),
                ('orchestrator', models.CharField(max_length=24)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessgroup',),
        ),
        migrations.CreateModel(
            name='DigitalResourceCommandRecord',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
                ('before_hash', models.CharField(max_length=64)),
                ('before_size', models.BigIntegerField(default=0)),
                ('after_hash', models.CharField(max_length=64)),
                ('after_size', models.BigIntegerField(default=0)),
                ('effect_status', models.CharField(max_length=1)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.AlterField(
            model_name='majoraartifactprocess',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processes', to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AlterField(
            model_name='majoraartifactprocessgroup',
            name='parent_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='process_groups', to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessgroup',
            name='root_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='process_leaves', to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AlterField(
            model_name='majoraartifact',
            name='primary_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_artifacts', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.CreateModel(
            name='MajoraMetaRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('meta_tag', models.CharField(max_length=64)),
                ('meta_name', models.CharField(max_length=64)),
                ('value_type', models.CharField(max_length=48)),
                ('value', models.CharField(max_length=128)),
                ('link', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField()),
                ('artifact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='metadata', to='majora2.MajoraArtifact')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='metadata', to='majora2.MajoraArtifactGroup')),
                ('pgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='metadata', to='majora2.MajoraArtifactProcessGroup')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majorametarecord_set+', to='contenttypes.ContentType')),
                ('process', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='metadata', to='majora2.MajoraArtifactProcess')),
                ('inheritable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='favourited', to='majora2.MajoraArtifactGroup')),
                ('pgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='favourited', to='majora2.MajoraArtifactProcessGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='majoraartifact',
            name='dice_name',
            field=models.CharField(blank=True, max_length=48, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='majoraartifactgroup',
            name='dice_name',
            field=models.CharField(blank=True, max_length=48, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='majoraartifactgroup',
            name='physical',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='majoraartifactgroup',
            name='processes',
            field=models.ManyToManyField(blank=True, related_name='tagged_processes', to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessgroup',
            name='dice_name',
            field=models.CharField(blank=True, max_length=48, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessgroup',
            name='meta_name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.CreateModel(
            name='BiosourceSamplingProcess',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('collection_location_adm0', models.CharField(blank=True, max_length=100, null=True)),
                ('collection_location_adm1', models.CharField(blank=True, max_length=100, null=True)),
                ('collection_by', models.CharField(blank=True, max_length=100, null=True)),
                ('collection_location_country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='BiosourceSamplingProcessRecord',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.AlterField(
            model_name='majoraartifactprocess',
            name='when',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='majoraartifactprocess',
            name='who',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='majoraartifact',
            name='root_artifact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='descendants', to='majora2.MajoraArtifact'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessrecord',
            name='in_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='before_process', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.AddField(
            model_name='majoraartifactprocessrecord',
            name='out_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='after_process', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.CreateModel(
            name='BiosampleExtractionProcess',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('extraction_method', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='BiosampleExtractionProcessRecord',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.AlterModelOptions(
            name='majoraartifactprocess',
            options={'ordering': ['-when']},
        ),
        migrations.RemoveField(
            model_name='majoraartifactprocess',
            name='group',
        ),
        migrations.CreateModel(
            name='MajoraArtifactQuarantinedProcess',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('note', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='MajoraArtifactQuarantinedProcessRecord',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
                ('note', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.AddField(
            model_name='majoraartifact',
            name='quarantined',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcessComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('when', models.DateTimeField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifactprocesscomment_set+', to='contenttypes.ContentType')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='majora2.MajoraArtifactProcess')),
                ('who', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-when'],
            },
        ),
        migrations.CreateModel(
            name='MajoraArtifactProcessRecordComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('when', models.DateTimeField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_majora2.majoraartifactprocessrecordcomment_set+', to='contenttypes.ContentType')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='majora2.MajoraArtifactProcessRecord')),
                ('who', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-when'],
            },
        ),
        migrations.CreateModel(
            name='MajoraArtifactUnquarantinedProcess',
            fields=[
                ('majoraartifactprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcess')),
                ('note', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocess',),
        ),
        migrations.CreateModel(
            name='MajoraArtifactUnquarantinedProcessRecord',
            fields=[
                ('majoraartifactprocessrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='majora2.MajoraArtifactProcessRecord')),
                ('note', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('majora2.majoraartifactprocessrecord',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=100)),
                ('ssh_key', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='biosampleartifact',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='biosamples', to='majora2.BiosourceSamplingProcess'),
        ),
        migrations.AlterField(
            model_name='biosampleartifact',
            name='sample_orig_id',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='majoraartifactgroup',
            name='unique_name',
            field=models.CharField(blank=True, max_length=48, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='majoraartifact',
            name='unique_name',
            field=models.CharField(blank=True, max_length=48, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='biosampleartifact',
            name='sample_type',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='biosampleartifact',
            name='specimen_type',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='majoraartifactprocess',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='processes', to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AlterField(
            model_name='majoraartifactprocessrecord',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='majora2.MajoraArtifactProcess'),
        ),
    ]
