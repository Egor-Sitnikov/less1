# Generated by Django 4.2.3 on 2023-08-14 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0002_advertisements_image_advertisements_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisements',
            name='image',
        ),
        migrations.RemoveField(
            model_name='advertisements',
            name='user',
        ),
    ]
