# Generated by Django 3.2.22 on 2023-11-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CH_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro_return_table',
            name='qty',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
