# Generated by Django 3.0.8 on 2020-07-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igem', '0013_auto_20200720_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regpeep',
            name='Gender',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
