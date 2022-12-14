# Generated by Django 4.0 on 2022-10-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableTeam',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('matches_played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lose', models.IntegerField()),
                ('goals_for', models.IntegerField()),
                ('goals_against', models.IntegerField()),
                ('goal_difference', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
            options={
                'db_table': 'table_22_23',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
