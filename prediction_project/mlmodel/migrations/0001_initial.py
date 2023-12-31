# Generated by Django 4.2.2 on 2023-07-04 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mlmodel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction_type', models.CharField(choices=[('Stone', 'Stone'), ('Panels', 'Panels'), ('Monolith', 'Monolith'), ('Cassette', 'Cassette'), ('Wooden', 'Wooden'), ('Bricks', 'Bricks')], max_length=8)),
                ('new_construction', mlmodel.models.ZeroOneBooleanField()),
                ('elevator', mlmodel.models.ZeroOneBooleanField()),
                ('floors_in_the_building', models.SmallIntegerField()),
                ('floor_area', models.FloatField()),
                ('number_of_rooms', models.SmallIntegerField()),
                ('number_of_bathrooms', models.SmallIntegerField()),
                ('ceiling_height', models.FloatField()),
                ('floor', models.SmallIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('balcony', models.CharField(choices=[('Open balcony', 'Open balcony'), ('Closed balcony', 'Closed balcony'), ('Not available', 'Not available'), ('Multiple balconies', 'Multiple balconies')], max_length=18)),
                ('furniture', models.CharField(choices=[('Available', 'Available'), ('Not available', 'Not available'), ('By agreement', 'By agreement'), ('Partial Furniture', 'Partial Furniture')], max_length=20)),
                ('renovation', models.CharField(choices=[('Major Renovation', 'Major Renovation'), ('Euro Renovation', 'Euro Renovation'), ('Old Renovation', 'Old Renovation'), ('No Renovation', 'No Renovation'), ('Designer Renovation', 'Designer Renovation'), ('Partial Renovation', 'Partial Renovation'), ('Cosmetic Renovation', 'Cosmetic Renovation')], max_length=24)),
                ('author', models.ForeignKey(default=mlmodel.models.get_or_create_public_user, on_delete=django.db.models.deletion.CASCADE, related_name='house', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
