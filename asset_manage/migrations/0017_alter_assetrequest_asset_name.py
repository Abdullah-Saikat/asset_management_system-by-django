# Generated by Django 4.1.4 on 2023-01-17 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_manage', '0016_alter_assetrequest_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetrequest',
            name='asset_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]