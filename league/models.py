from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    avatar = models.URLField(null=True, blank=False, unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

class Stadium(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    capacity = models.IntegerField(null=True)

class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    home_stadium = models.ForeignKey(Stadium, unique=False, null=True, on_delete=models.SET_NULL)

class Match(models.Model):
    home_team = models.ForeignKey(Team, unique=False, null=False, on_delete=models.PROTECT, related_name="home_team")
    away_team = models.ForeignKey(Team, unique=False, null=False, on_delete=models.PROTECT, related_name="away_team")
    home_team_goals = models.IntegerField(null=True)
    away_team_goals = models.IntegerField(null=True)
    begin_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    stadium = models.ForeignKey(Stadium, null=False, unique=False, on_delete=models.PROTECT)
    match_round = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(36)])
    game_played = models.BooleanField(null=False, default=False)

class Comment(models.Model):
    text = models.TextField(blank=False, max_length=10000, unique=False)
    user = models.ForeignKey(User, unique=False, null=False, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    match_round = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(36)])


class TableTeam(models.Model):
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


