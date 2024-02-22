# Generated by Django 4.0.4 on 2024-02-09 19:01

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_alter_author_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
