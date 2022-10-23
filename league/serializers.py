from rest_framework import serializers

from league.models import TableTeam, Team


class TableTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = TableTeam
        fields = "__all__"

class TableSerializer(serializers.Serializer):
    teams = TableTeamSerializer(many=True)

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"