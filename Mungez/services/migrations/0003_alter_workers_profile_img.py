# Generated by Django 5.2.4 on 2025-07-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_workers_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='profile_img',
            field=models.ImageField(default='images/default.jpg', upload_to=''),
        ),
    ]
