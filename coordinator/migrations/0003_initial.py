# Generated by Django 4.2.3 on 2023-07-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coordinator', '0002_delete_requesttoreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_number', models.CharField(max_length=12)),
                ('reviewer_1_email', models.EmailField(max_length=254)),
                ('reviewer_2_email', models.EmailField(max_length=254)),
                ('reviewer_3_email', models.EmailField(max_length=254)),
                ('reviewer_4_email', models.EmailField(max_length=254)),
                ('reviewer_5_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
