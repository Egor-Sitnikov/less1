# Generated by Django 4.2.3 on 2023-08-14 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0005_remove_advertisements_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisements',
            name='user',
        ),
    ]