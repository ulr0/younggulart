# Generated by Django 3.2 on 2021-05-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='framematerial',
            name='image_url',
            field=models.URLField(default='#', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='framesize',
            name='price_rise_rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='framesize',
            name='thickness_cm',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=4),
            preserve_default=False,
        ),
    ]
