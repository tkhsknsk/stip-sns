# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-09 09:18


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0014_auto_20171110_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='sharing_people',
            field=models.ManyToManyField(related_name='feed_sharing_people', to='authentication.Profile'),
        ),
    ]
