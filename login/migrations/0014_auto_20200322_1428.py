# Generated by Django 3.0.2 on 2020-03-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_userprofile_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=None, verbose_name='date account created'),
        ),
    ]
