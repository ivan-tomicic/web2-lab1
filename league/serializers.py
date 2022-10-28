import logging

from rest_framework import serializers

from league.models import TableTeam, Team, Comment

logger = logging.getLogger('error')

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

class CommentSerializer(serializers.ModelSerializer):

    text = serializers.CharField(required=True, min_length=2)
    match_round = serializers.IntegerField(required=True)

    class Meta:
        model = Comment
        fields = ('text', 'match_round')

    def create(self, validated_data):
        try:
            user_id = self.context['user_id']
            username = self.context['username']
            comment = Comment.objects.create(user_id=user_id, username=username, **validated_data)

            return comment

        except Exception as e:
            logger.error(e)
            raise Exception

    def update(self):
        comment = Comment.objects.filter(id=self.context["comment_id"], user_id=self.context["user_id"]).update(text=self.data["text"])
        return comment



