# Generated by Django 4.1.5 on 2023-03-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
