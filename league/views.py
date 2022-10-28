import json, logging

from django.db import transaction, Error
from django.db.models import Count, Case, When, Q, F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response

from league.models import TableTeam, Match, Comment
from league.serializers import CommentSerializer

logger = logging.getLogger('info')


def index(request):
    table_teams = [table_team for table_team in
                   TableTeam.objects.order_by("-points", "-goal_difference", "-goals_for").values()]
    match_rounds = [r for r in
                    Match.objects.values("match_round").annotate(played=Count(Case(When(game_played=True, then=1))),
                                                                 not_played=Count(
                                                                     Case(When(game_played=False, then=1)))).order_by(
                        "match_round")]

    print(json.dumps(request.session.get("user"), indent=4))
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


@api_view(['GET'])
def match_round(request, match_round):
    matches = [m for m in Match.objects.filter(match_round=match_round).order_by("-game_played").annotate(
        home_team_name=F('home_team__name'),
        away_team_name=F('away_team__name'),
        home_team_photo=F('home_team__photo_url'),
        away_team_photo=F('away_team__photo_url')).values()]

    comments = Comment.objects.filter(match_round=match_round).order_by("-created_on")
    return render(
        request,
        "match_round.html",
        context={
            "session": request.session.get("user"),
            "round_number": match_round,
            "matches": matches,
            "comments": comments if request.session.get("user") else None,
        },
    )


class CommentView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @transaction.atomic
    def create(self, request):
        user_id = request.session.get("user").get("userinfo").get("sub")
        username = request.session.get("user").get("userinfo").get("name")

        comment_serializer = CommentSerializer(data=request.data,
                                             context={'user_id': user_id, 'username': username})
        if comment_serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    comment_serializer.save()


            except Error as error:
                transaction.set_rollback(True)
                return Response("Error when saving comment to database.", status=status.HTTP_400_BAD_REQUEST)
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

