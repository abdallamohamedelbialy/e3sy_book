# Generated by Django 4.2.7 on 2023-12-03 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=3, default=2, max_digits=5),
            preserve_default=False,
        ),
    ]