# Generated by Django 2.1.4 on 2018-12-13 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(blank=True, max_length=100, null=True, verbose_name='organisation')),
                ('repo_name', models.CharField(max_length=30, verbose_name='repo_name')),
                ('src', models.URLField(max_length=100, verbose_name='repo_src')),
                ('owner', models.CharField(max_length=100, verbose_name='owner')),
                ('date_crea', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('accept', models.BooleanField(default=True)),
            ],
        ),
    ]
