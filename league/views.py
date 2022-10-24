import json, logging

from django.db.models import Count, Case, When, Q, F
from django.http import HttpResponse
from django.shortcuts import render

from league.models import TableTeam, Match

logger = logging.getLogger('info')


def index(request):
    logger.info(request.session.get("user"))
    table_teams = [table_team for table_team in TableTeam.objects.order_by("-points", "-goal_difference", "-goals_for").values()]
    match_rounds = [r for r in Match.objects.values("match_round").annotate(played=Count(Case(When(game_played=True, then=1))),
                                                                     not_played=Count(Case(When(game_played=False, then=1)))).order_by("match_round")]

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "teams": table_teams,
            "match_rounds": match_rounds
        },
    )

def match_round(request, match_round):
    logger.info('round')
    logger.info(match_round)

    matches = [m for m in Match.objects.filter(match_round=match_round).order_by("game_played").annotate(home_team_name=F('home_team__name'),
                                                                                                         away_team_name=F('away_team__name'),
                                                                                                         home_team_photo=F('home_team__photo_url'),
                                                                                                         away_team_photo=F('away_team__photo_url')).values()]
    print(matches)
    return render(
        request,
        "match_round.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "round_number": match_round,
            "matches": matches
        },
    )





