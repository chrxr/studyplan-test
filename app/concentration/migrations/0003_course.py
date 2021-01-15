# Generated by Django 3.1.5 on 2021-01-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentration', '0002_requirement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('requirement', models.ManyToManyField(to='concentration.Requirement')),
            ],
        ),
    ]
