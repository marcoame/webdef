# Generated by Django 4.1.5 on 2023-03-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0014_delete_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id_project', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]