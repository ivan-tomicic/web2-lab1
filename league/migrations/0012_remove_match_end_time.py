# Generated by Django 4.0 on 2022-10-28 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0011_comment_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='end_time',
        ),
    ]