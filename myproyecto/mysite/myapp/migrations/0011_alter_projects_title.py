# Generated by Django 4.1.5 on 2023-03-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]