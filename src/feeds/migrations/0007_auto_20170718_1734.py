# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-18 08:34


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_auto_20170714_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='file',
            new_name='files',
        ),
    ]
