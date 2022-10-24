from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    photo_url = models.URLField(null=True)

class Match(models.Model):
    home_team = models.ForeignKey(Team, unique=False, null=False, on_delete=models.PROTECT, related_name="home_team")
    away_team = models.ForeignKey(Team, unique=False, null=False, on_delete=models.PROTECT, related_name="away_team")
    home_team_goals = models.IntegerField(null=True)
    away_team_goals = models.IntegerField(null=True)
    begin_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    match_round = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(36)])
    game_played = models.BooleanField(null=False, default=False)

class Comment(models.Model):
    text = models.TextField(blank=False, max_length=10000, unique=False)
    username = models.CharField(max_length=200, null=False)
    user_id = models.CharField(max_length=200, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    match_round = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(36)])


class TableTeam(models.Model):
    photo_url = models.URLField()
    name = models.TextField(primary_key=True)
    matches_played = models.IntegerField()
    win = models.IntegerField()
    draw = models.IntegerField()
    lose = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    goal_difference = models.IntegerField()
    points = models.IntegerField()
    class Meta:
        managed = False
        db_table = "table_22_23"


