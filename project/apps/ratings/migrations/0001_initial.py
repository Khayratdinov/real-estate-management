# Generated by Django 5.0.3 on 2024-09-25 12:01

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "Very Poor"),
                            (2, "Poor"),
                            (3, "Average"),
                            (4, "Good"),
                            (5, "Excellent"),
                        ],
                        verbose_name="Rating",
                    ),
                ),
                ("comment", models.TextField(blank=True, verbose_name="Comment")),
                (
                    "rated_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_ratings",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Rated User",
                    ),
                ),
                (
                    "rating_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="given_ratings",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Rating User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rating",
                "verbose_name_plural": "Ratings",
            },
        ),
    ]
