# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-02-12 08:15


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0021_auto_20181010_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='files',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='sharing_group',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='sharing_people',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='user',
        ),
        migrations.DeleteModel(
            name='AttachFile',
        ),
        migrations.DeleteModel(
            name='Feed',
        ),
    ]
