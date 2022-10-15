from django.db import models


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


class Season(models.Model):
    begin_year = models.IntegerField(null=False)
    end_year = models.IntegerField(null=False)
    number_of_rounds = models.IntegerField(null=False)
    teams = models.ManyToManyField(Team)


class MatchRound(models.Model):
    number = models.IntegerField(null=False)
    season = models.ForeignKey(Season, null=False, on_delete=models.PROTECT)

class Match(models.Model):
    home_team = models.ForeignKey(Team, unique=False, null=False, on_delete=models.PROTECT, related_name="home_team")
    away_team = models.ForeignKey(Team, unique=False, null=False, on_delete=models.PROTECT, related_name="away_team")
    begin_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    stadium = models.ForeignKey(Stadium, null=False, unique=False, on_delete=models.PROTECT)

class Comment(models.Model):
    text = models.TextField(blank=False, max_length=10000, unique=False)
    user = models.ForeignKey(User, unique=False, null=False, on_delete=models.CASCADE)
    match_round = models.ForeignKey(MatchRound, unique=False, null=True, on_delete=models.CASCADE)


