# Generated by Django 5.0.6 on 2024-05-22 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_like_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like_by',
            new_name='liked_by',
        ),
    ]