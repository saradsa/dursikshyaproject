# Generated by Django 4.1.7 on 2023-06-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stroll1", "0010_rename_product_destination_remove_orderitem_order_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="review",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
