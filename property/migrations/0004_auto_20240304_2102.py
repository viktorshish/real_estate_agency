# Generated by Django 2.2.24 on 2024-03-04 18:02

from django.db import migrations


def fill_new_bulding_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__lte=2015).update(new_building=False)
    Flat.objects.filter(construction_year__gt=2015).update(new_building=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_bulding_field)
    ]
