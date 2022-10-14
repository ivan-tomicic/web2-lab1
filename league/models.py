from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)

class Manager(Person):
    pass
class Player(Person):
    pass

class Stadium(models.Model):
    pass

class Team(models.Model):
    pass

class Match(models.Model):
    pass