# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-30 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("parties", "0004_auto_20170530_1520")]

    operations = [
        migrations.AlterModelOptions(
            name="manifesto", options={"ordering": ["-country", "language"]}
        ),
        migrations.AlterField(
            model_name="manifesto",
            name="country",
            field=models.CharField(
                choices=[
                    ("UK", "UK"),
                    ("England", "England"),
                    ("Scotland", "Scotland"),
                    ("Wales", "Wales"),
                    ("Northern Ireland", "Northern Ireland"),
                ],
                default="UK",
                max_length=200,
            ),
        ),
    ]
