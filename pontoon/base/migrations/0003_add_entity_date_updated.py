# Generated by Django 2.2.11 on 2020-05-08 20:55

from django.db import migrations, models
from django.db.models import F
import django.utils.timezone


def set_default_date_updated(apps, schema_editor):
    """Initialize date_updated to the value of date_created (instead of now(), which is the model default)
    """
    Entity = apps.get_model("base", "entity")
    Entity.objects.all().update(date_updated=F("date_created"))


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_auto_20200322_1821"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="date_updated",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RunPython(set_default_date_updated, migrations.RunPython.noop),
    ]