# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-09 06:20


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20170914_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[(b'admin', 'ROLE_CHOICE_admin'), (b'user', 'ROLE_CHOICE_user'), (b'machine', 'ROLE_CHOICE_machine'), (b'machine_feed_only', 'ROLE_CHOICE_machine_feed_only'), (b'machine_bot', 'ROLE_CHOICE_machine_bot')], default='user', max_length=10),
        ),
    ]
