# Generated by Django 4.0.3 on 2022-07-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]