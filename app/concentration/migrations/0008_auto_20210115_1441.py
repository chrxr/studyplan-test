# Generated by Django 3.1.5 on 2021-01-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentration', '0007_auto_20210115_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concentration',
            name='requirement',
            field=models.ManyToManyField(related_name='concentrations', to='concentration.Requirement'),
        ),
    ]
