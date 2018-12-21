# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("elections", "0020_postelection_ballot_paper_id"),
        ("people", "0026_auto_20180417_1944"),
    ]

    operations = [
        migrations.CreateModel(
            name="CandidatePledge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField(blank=True)),
                ("answer", models.TextField(blank=True)),
                (
                    "ballot_paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elections.PostElection",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="people.Person"
                    ),
                ),
            ],
        )
    ]
