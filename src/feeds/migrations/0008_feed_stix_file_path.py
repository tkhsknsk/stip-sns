# Generated by Django 1.10.4 on 2017-07-20 22:50


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_auto_20170718_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='stix_file_path',
            field=models.FilePathField(default=None, max_length=1024, null=True),
        ),
    ]
