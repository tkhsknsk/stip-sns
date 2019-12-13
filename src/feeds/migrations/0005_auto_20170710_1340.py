# Generated by Django 1.10.4 on 2017-07-10 04:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_feed_tlp'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='title',
            field=models.TextField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='post',
            field=models.TextField(max_length=10240),
        ),
    ]
