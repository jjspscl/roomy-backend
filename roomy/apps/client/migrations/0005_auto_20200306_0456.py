# Generated by Django 3.0.3 on 2020-03-06 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20200304_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=56),
        ),
    ]