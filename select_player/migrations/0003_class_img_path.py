# Generated by Django 3.1.7 on 2021-03-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_player', '0002_item_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='img_path',
            field=models.TextField(default=''),
        ),
    ]
