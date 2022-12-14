# Generated by Django 4.0 on 2022-10-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_remove_season_teams_match_match_round_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-02 16:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_goals',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_goals',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
