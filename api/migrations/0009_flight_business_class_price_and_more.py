# Generated by Django 5.1.3 on 2024-11-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_airport_options_alter_board_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='business_class_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='flight',
            name='economy_class_price',
            field=models.FloatField(default=0.0),
        ),
    ]
