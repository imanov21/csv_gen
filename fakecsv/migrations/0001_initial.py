# Generated by Django 3.1.1 on 2020-09-21 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('column_separator', models.CharField(max_length=100, verbose_name='Column separator')),
                ('string_character', models.CharField(max_length=100, verbose_name='String character')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('range_from', models.PositiveIntegerField()),
                ('range_to', models.PositiveIntegerField()),
                ('order', models.PositiveIntegerField()),
                ('data_type', models.CharField(choices=[('FN', 'Full name'), ('JOB', 'Job'), ('EMAIL', 'Email'), ('DOMAIN', 'Domain'), ('PN', 'Phone number'), ('CN', 'Company name'), ('INT', 'Integer'), ('ADDR', 'Address'), ('DATE', 'Date')], max_length=10)),
                ('data_schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fakecsv.dataschema')),
            ],
        ),
    ]
