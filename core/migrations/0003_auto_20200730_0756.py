# Generated by Django 2.2.3 on 2020-07-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_auto_20200730_0746"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semester",
            name="semester",
            field=models.CharField(
                blank=True,
                choices=[("First", "First"), ("Second", "Second"), ("Third", "Third")],
                max_length=10,
            ),
        ),
    ]

