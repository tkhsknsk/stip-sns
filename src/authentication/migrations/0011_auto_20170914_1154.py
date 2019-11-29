# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-14 02:54


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_profile_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ci',
            field=models.CharField(choices=[(b'Information and Communication Services', 'CI_Information and Communication Services'), (b'Financial Services', 'CI_Financial Services'), (b'Aviation Services', 'CI_Aviation Services'), (b'Railway Services', 'CI_Railway Services'), (b'Electric Power Supply Services', 'CI_Electric Power Supply Services'), (b'Gas Supply Services', 'CI_Gas Supply Services'), (b'Government and Administrative Services (Including Municipal Government)', 'CI_Government and Administrative Services (Including Municipal Government)'), (b'Medical Services', 'CI_Medical Services'), (b'Water Services', 'CI_Water Services'), (b'Logistics Services', 'CI_Logistics Services'), (b'Chemical Industries', 'CI_Chemical Industries'), (b'Credit Card Services', 'CI_Credit Card Services'), (b'Petroleum Industries', 'CI_Petroleum Industries'), (b'Other', 'CI_Other')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[(b'en', 'English'), (b'pt-br', 'Portuguese'), (b'es', 'Spanish'), (b'ja', 'Japanese'), (b'fr', 'French'), (b'zh-cn', 'Chinese')], default='en', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sector',
            field=models.CharField(choices=[(b'chemical', 'SECTOR_GROUP_Chemical Sector'), (b'commercial', 'SECTOR_GROUP_Commercial Facilities Sector'), (b'communication', 'SECTOR_GROUP_Communications Sector'), (b'critical', 'SECTOR_GROUP_Critical Manufacturing Sector'), (b'dams', 'SECTOR_GROUP_Dams Sector'), (b'defense', 'SECTOR_GROUP_Defense Industrial Base Sector'), (b'emergency', 'SECTOR_GROUP_Emergency Services Sector'), (b'energy', 'SECTOR_GROUP_Energy Sector'), (b'financial', 'SECTOR_GROUP_Financial Services Sector'), (b'food', 'SECTOR_GROUP_Food and Agriculture Sector'), (b'government', 'SECTOR_GROUP_Government Facilities Sector'), (b'healthcare', 'SECTOR_GROUP_Healthcare and Public Health Sector'), (b'information', 'SECTOR_GROUP_Information Technology Sector'), (b'nuclear', 'SECTOR_GROUP_Nuclear Reactors, Materials, and Waste Sector'), (b'other', 'SECTOR_GROUP_Other'), (b'transport', 'SECTOR_GROUP_Transportation Systems Sector'), (b'water', 'SECTOR_GROUP_Water and Wastewater Systems Sector')], max_length=128, null=True),
        ),
    ]
