# Generated by Django 3.0.3 on 2020-04-05 06:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettertemplate',
            name='template',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
