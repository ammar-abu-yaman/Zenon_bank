# Generated by Django 3.0.7 on 2020-10-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201003_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='static/default.png', upload_to='static/profile_images'),
        ),
    ]
