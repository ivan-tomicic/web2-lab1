import json, logging

from django.db.models import Count, Case, When
from django.http import HttpResponse
from django.shortcuts import render

from league.models import TableTeam, Match

logger = logging.getLogger('info')


def index(request):
    logger.info(request.session.get("user"))
    table_teams = [table_team for table_team in TableTeam.objects.order_by("-points", "-goal_difference", "-goals_for").values()]
    match_rounds = [round for round in Match.objects.values("match_round").annotate(played=Count(Case(When(game_played=True, then=1))),
                                                                     not_played=Count(Case(When(game_played=False, then=1)))).order_by("match_round")]
    print(match_rounds)

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





