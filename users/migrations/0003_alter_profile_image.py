# Generated by Django 3.2.5 on 2021-07-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='C:/Users/RAJ KUMAR/Desktop/Django_Apps/django_apps/media/default.jpg', upload_to='profile_pics'),
        ),
    ]
