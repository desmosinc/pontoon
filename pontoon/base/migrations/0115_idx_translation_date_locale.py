# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-09 22:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0114_project_path_unique"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="translation",
            index_together=set(
                [
                    ("entity", "locale", "approved"),
                    ("entity", "user"),
                    ("entity", "locale", "fuzzy"),
                    ("date", "locale"),
                ]
            ),
        ),
    ]
