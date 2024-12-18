# Generated by Django 5.0.3 on 2024-03-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app", models.TextField()),
                ("enduser", models.TextField()),
                ("sess", models.TextField()),
                ("msg", models.TextField()),
                ("speaker", models.TextField()),
                ("ts", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
