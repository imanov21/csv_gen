# Generated by Django 3.1.1 on 2020-09-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakecsv', '0003_auto_20200922_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataschema',
            name='string_character',
            field=models.CharField(choices=[('"', 'Double qoute (")'), ("'", "Single quote (')")], max_length=100, verbose_name='String character'),
        ),
    ]