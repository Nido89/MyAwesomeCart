# Generated by Django 3.0.3 on 2020-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200325_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default='0', max_length=100),
        ),
    ]
