# Generated by Django 3.0.7 on 2020-06-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QrCodeBase', '0004_auto_20200618_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codehandler',
            name='profile_id',
            field=models.IntegerField(blank=True, max_length=24, null=True),
        ),
    ]
