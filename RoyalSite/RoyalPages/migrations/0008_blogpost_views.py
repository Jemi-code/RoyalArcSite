# Generated by Django 3.2.3 on 2021-07-10 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoyalPages', '0007_auto_20210707_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
