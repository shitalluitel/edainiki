# Generated by Django 3.0.3 on 2020-03-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LetterTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('Charkilla', 'Charkilla'), ('Student', 'Student')], default='Charkilla', max_length=120)),
                ('template', models.TextField(max_length=10000)),
                ('type', models.CharField(choices=[('Nibedan', 'Nibedan'), ('Sifaris', 'Sifaris')], max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
