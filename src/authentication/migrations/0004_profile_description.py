# Generated by Django 1.10.4 on 2017-07-13 23:02


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_affiliation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
