# Generated by Django 3.2 on 2021-04-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0008_auto_20210430_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='biddinguser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
