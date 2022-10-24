# Generated by Django 4.0 on 2022-10-24 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_match_game_played_alter_match_away_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='away_team', to='league.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='home_team', to='league.team'),
            preserve_default=False,
        ),
    ]