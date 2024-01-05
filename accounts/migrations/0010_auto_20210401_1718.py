# Generated by Django 3.1.3 on 2023-12-21 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200906_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]

