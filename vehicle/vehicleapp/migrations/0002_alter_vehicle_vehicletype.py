# Generated by Django 4.2 on 2023-04-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicleType',
            field=models.IntegerField(choices=[(2, 'twowheeler'), (3, 'threewheeler'), (4, 'fourwheeler')], default=2),
        ),
    ]
