# Generated by Django 3.0.8 on 2020-07-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igem', '0009_auto_20200717_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfolder',
            name='File_to_upload',
            field=models.FileField(upload_to='coursemat/media/'),
        ),
    ]