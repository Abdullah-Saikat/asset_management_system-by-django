# Generated by Django 4.0.2 on 2022-12-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_manage', '0009_asset_asset_quantity_assetinfo_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetinfo',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]