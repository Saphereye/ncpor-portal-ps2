# Generated by Django 4.2.3 on 2023-07-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_details_address_details_designation_details_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='is_coordinator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='details',
            name='is_pi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='details',
            name='is_verifier',
            field=models.BooleanField(default=False),
        ),
    ]
