# Generated by Django 3.0.7 on 2020-09-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_file_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='state',
            field=models.CharField(choices=[("('A',)", 'Accepted'), ('P', 'Pending'), ('D', 'Denied')], default='D', max_length=10),
        ),
    ]
