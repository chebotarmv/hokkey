from rest_framework import serializers

from .models import KhlTeam, KhlGameStat


class KhlTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhlTeam
        fields = '__all__'


class KhlGameStatSerializer(serializers.ModelSerializer):
    khlteam = KhlTeamSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = KhlGameStat
        fields = '__all__'
