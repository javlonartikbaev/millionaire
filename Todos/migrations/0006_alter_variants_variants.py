# Generated by Django 5.0.6 on 2024-05-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todos', '0005_rename_restaurant_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='variants',
            field=models.JSONField(default=list),
        ),
    ]
