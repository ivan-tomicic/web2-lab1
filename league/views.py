import json, logging
import os

from django.db import transaction, Error
from django.db.models import Count, F, DateTimeField, CharField
from django.db.models.functions import TruncSecond, Cast
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.response import Response

from league.models import TableTeam, Match, Comment, Team
from league.serializers import CommentSerializer, MatchSerializer

logger = logging.getLogger('info')




@api_view(['GET'])
def index(request):
    table_teams = [table_team for table_team in
                   TableTeam.objects.order_by("-points", "-goal_difference", "-goals_for").values()]
    match_rounds = [r for r in Match.objects.values("match_round").annotate(played=Count('id')).order_by("match_round")]

    user = request.session.get("user")
    is_admin = False
    if user:
        is_admin = os.getenv("ADMIN_ID") == user.get("userinfo").get("sub")
    return render(
        request,
        "index.html",
        context={
            "session": user,
            "pretty": json.dumps(user, indent=4),
            "teams": table_teams,
            "match_rounds": match_rounds,
            "is_admin": is_admin
        },
    )


@api_view(['GET'])
def match_round(request, match_round):
    matches = [m for m in Match.objects.filter(match_round=match_round).annotate(
        home_team_name=F('home_team__name'),
        away_team_name=F('away_team__name'),
        home_team_photo=F('home_team__photo_url'),
        away_team_photo=F('away_team__photo_url')).values()]

    comments = Comment.objects.filter(match_round=match_round).order_by("-created_on")
    user = request.session.get("user")
    is_admin = False
    if user:
        is_admin = os.getenv("ADMIN_ID") == user.get("userinfo").get("sub")
    return render(
        request,
        "match_round.html",
        context={
            "session": user,
            "round_number": match_round,
            "matches": matches,
            "comments": comments if request.session.get("user") else None,
            "is_admin": is_admin


        },
    )


class CommentView(viewsets.ModelViewSet):
    http_method_names = ['post', 'put', 'delete']
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


    def destroy(self, request, pk=None):
        user_id = request.session.get("user").get("userinfo").get("sub")
        try:
            if user_id == os.getenv("ADMIN_ID"):
                Comment.objects.filter(id=pk).delete()
            else:
                Comment.objects.get(id=pk, user_id=user_id).delete()
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    def update(self, request, pk=None):
        user_id = request.session.get("user").get("userinfo").get("sub")
        comment_serializer = CommentSerializer(data=request.data,
                                               context={'user_id': user_id, 'comment_id': pk})
        if comment_serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    comment_serializer.update()
            except Error as error:
                transaction.set_rollback(True)
                return Response("Error when updating comment", status=status.HTTP_400_BAD_REQUEST)
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatchView(viewsets.ModelViewSet):
    http_method_names = ['post', 'put', 'delete']
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


@api_view(['GET'])
def edit_match_view(request):
    all_matches = Match.objects.all()
    teams = Team.objects.all().values('id', 'name').order_by('id')
    matche_rounds = []
    for match_round in all_matches.values_list('match_round', flat=True).distinct():
        matche_rounds.append({
            'match_round': match_round,
            'matches': list(all_matches.filter(match_round=match_round)
                               .annotate(begin_time_str=Cast(TruncSecond('begin_time', DateTimeField()), CharField()))
                               .values())

        })
    print(matche_rounds)

    user = request.session.get("user")
    is_admin = False
    if user:
        is_admin = os.getenv("ADMIN_ID") == user.get("userinfo").get("sub")
    return render(
        request,
        "edit_match.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "matches_rounds": matche_rounds,
            "is_admin": is_admin,
            "teams": teams
        },
    )


