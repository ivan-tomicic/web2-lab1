import json, logging

from django.http import HttpResponse
from django.shortcuts import render

from league.models import TableTeam, Team
from league.serializers import TableTeamSerializer, TeamSerializer, TableSerializer

logger = logging.getLogger('info')


def index(request):
    logger.info(request.session.get("user"))
    table_teams = [table_team for table_team in TableTeam.objects.order_by("-points", "-goal_difference", "-goals_for").values()]

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "teams": table_teams
        },
    )




