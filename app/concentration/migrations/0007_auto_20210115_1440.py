# Generated by Django 3.1.5 on 2021-01-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentration', '0006_auto_20210114_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concentration',
            name='requirement',
            field=models.ManyToManyField(related_name='requirements', to='concentration.Requirement'),
        ),
    ]
