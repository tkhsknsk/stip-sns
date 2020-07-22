# Generated by Django 1.10.4 on 2017-07-31 07:32


from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0008_feed_stix_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='sharing_group',
            field=models.CharField(choices=[(b'information', b'Information and communication services'), (b'financial', b'Financial services'), (b'aviation', b'Aviation services'), (b'railway', b'Railway services'), (b'electric', b'Electric power supply services'), (b'gas', b'Gas supply services'), (b'government', b'Government and administrative services'), (b'medical', b'Medical services'), (b'water', b'Water services'), (b'logistics', b'Logistics services'), (b'chemical', b'Chemical industries'), (b'credit', b'Credit card services'), (b'petroleum', b'Petroleum industries')], default=b'csc', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='sharing_people',
            field=models.ManyToManyField(related_name='feed_sharing_people', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='sharing_range_type',
            field=models.CharField(choices=[(b'all', b'With All'), (b'group', b'With a group'), (b'people', b'With people')], default=b'all', max_length=10),
        ),
    ]
