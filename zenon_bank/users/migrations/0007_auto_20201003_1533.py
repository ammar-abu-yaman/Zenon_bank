# Generated by Django 3.0.7 on 2020-10-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201003_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default.png', upload_to='static/profile_images'),
        ),
    ]
