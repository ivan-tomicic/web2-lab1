# Generated by Django 4.0 on 2022-10-24 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_tableteam_delete_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='game_played',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='away_team', to='league.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team_goals',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='begin_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='home_team', to='league.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_goals',
            field=models.IntegerField(null=True),
        ),
    ]