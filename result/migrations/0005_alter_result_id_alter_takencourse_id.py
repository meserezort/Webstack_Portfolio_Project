# Generated by Django 4.1.6 on 2023-02-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20200825_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
