# Generated by Django 3.2.5 on 2021-07-28 20:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg'])]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg'])]),
        ),
    ]