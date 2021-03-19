# Generated by Django 3.0.3 on 2020-03-15 17:12

import apps.common.validators.commons
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charkilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('applicant_name', models.CharField(error_messages={'max_length': 'कृपया नामाको लम्बाई ६४ भन्दा कम राख्नुहोस।'}, max_length=150)),
                ('eng_date', models.DateField(null=True)),
                ('nep_date', models.CharField(error_messages={'max_length': 'तपाईले छान्नु भएको मिति मिलेको छैन। कृपया सहि मिति छनोट गर्नुहोस्।'}, max_length=10, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('form_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharkillaDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitta_no', models.CharField(error_messages={'max_length': 'कृपया कित्ता नंको लम्बाई १६ भन्दा कम राख्नुहोस।'}, max_length=16)),
                ('map_sheet_no', models.CharField(error_messages={'max_length': 'कृपया कित्ता नंको लम्बाई १६ भन्दा कम राख्नुहोस।'}, max_length=16)),
                ('total_area', models.CharField(max_length=8, validators=[apps.common.validators.commons.area_validation])),
                ('east_piller', models.CharField(error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'}, max_length=132)),
                ('west_piller', models.CharField(error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'}, max_length=132)),
                ('north_piller', models.CharField(error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'}, max_length=132)),
                ('south_piller', models.CharField(error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'}, max_length=132)),
                ('description', models.CharField(blank=True, error_messages={'max_length': 'कृपया कैफियतको लम्बाई २५० भन्दा कम राख्नुहोस |'}, max_length=264, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('charkilla', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='charkilla_details', to='charkilla.Charkilla')),
            ],
        ),
    ]