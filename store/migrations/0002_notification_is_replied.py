# Generated by Django 5.0.1 on 2024-04-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_replied',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
