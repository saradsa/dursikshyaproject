# Generated by Django 4.2.1 on 2023-05-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stroll1", "0004_blogs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="description",
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
