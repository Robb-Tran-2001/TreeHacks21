# Generated by Django 3.1.6 on 2021-02-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210213_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_ppoi',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
