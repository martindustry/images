# Generated by Django 4.1.3 on 2022-11-22 11:58

from django.core.management import call_command
from django.db import migrations


def load_fixtures(apps, schema_editor):
    call_command("loaddata", "fixtures/builtin_tiers.json")


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_fixtures),
    ]