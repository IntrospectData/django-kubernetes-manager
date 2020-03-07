# Generated by Django 3.0.3 on 2020-02-28 01:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_kubernetes_manager', '0010_auto_20200226_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetcluster',
            name='config',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Configuration data stored as an encrypted blob in the database', null=True),
        ),
    ]