# Generated by Django 4.2.1 on 2023-05-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stroll1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Custom",
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
                ("name", models.CharField(max_length=100)),
                ("destnation", models.CharField(max_length=100)),
                ("activity", models.CharField(max_length=100)),
                ("duration", models.CharField(max_length=100)),
                ("date", models.CharField(max_length=100)),
            ],
        ),
    ]
