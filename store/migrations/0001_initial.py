# Generated by Django 5.0.1 on 2024-03-26 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='vehicle_images')),
                ('decription', models.TextField(null=True)),
                ('category', models.CharField(choices=[('motorbike', 'motorbike'), ('scooter', 'scooter')], default='motorbike', max_length=30)),
                ('fuel', models.CharField(choices=[('petrol', 'petrol'), ('electric', 'electric')], default='petrol', max_length=20)),
                ('kms', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('owner_type', models.CharField(choices=[('first_hand', 'first_hand'), ('second_hand', 'second_hand'), ('third_hand', 'third_hand'), ('fourth_hand', 'fourth_hand'), ('other', 'other')], default=None, max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('is_sold', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('brand_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='store.brand')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('is_read', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('vehicle_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='store.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('owner_object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
                ('vehicle_objects', models.ManyToManyField(related_name='wishlist_item', to='store.vehicle')),
            ],
        ),
    ]