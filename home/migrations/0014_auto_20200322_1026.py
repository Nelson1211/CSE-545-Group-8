# Generated by Django 3.0.2 on 2020-03-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200322_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=4459937243, max_length=10, unique=True),
        ),
    ]