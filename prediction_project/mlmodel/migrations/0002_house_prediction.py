# Generated by Django 4.2.2 on 2023-07-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='prediction',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
    ]
