# Generated by Django 2.2.3 on 2020-08-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200822_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='default.png', null=True, upload_to='profile_pictures/%y/%m/%d/'),
        ),
    ]

