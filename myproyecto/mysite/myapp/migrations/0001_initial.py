# Generated by Django 4.1.5 on 2023-02-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id_project', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('publishable', models.CharField(max_length=50)),
            ],
        ),
    ]
