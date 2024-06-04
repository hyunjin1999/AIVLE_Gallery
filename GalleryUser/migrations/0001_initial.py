# Generated by Django 5.0.6 on 2024-06-03 11:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "username",
                    models.CharField(
                        db_column="user_id",
                        max_length=200,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("password", models.CharField(db_column="PW", max_length=200)),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "is_superuser",
                    models.IntegerField(blank=True, default=False, null=True),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, db_column="e_mail", max_length=320, null=True
                    ),
                ),
                ("is_active", models.IntegerField(blank=True, default=True, null=True)),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
    ]
