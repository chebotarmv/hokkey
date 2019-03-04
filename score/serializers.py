from rest_framework import serializers

from .models import KhlTeam, KhlGameStat, NhlTeam, NhlGameStat


class KhlTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhlTeam
        fields = '__all__'


class KhlGameStatSerializer(serializers.ModelSerializer):
    khlteam = KhlTeamSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = KhlGameStat
        fields = '__all__'


class NhlTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model =NhlTeam
        fields = '__all__'


class NhlGameStatSerializer(serializers.ModelSerializer):
    nhlteam = NhlTeamSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = NhlGameStat
        fields = '__all__'
