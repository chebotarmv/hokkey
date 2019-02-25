from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import KhlTeam, KhlGameStat
from .serializers import KhlTeamSerializer, KhlGameStatSerializer


class TeamsList(APIView):
    def get(self, request):
        teams = KhlTeam.objects.all()
        data = KhlTeamSerializer(teams, many=True).data
        return Response(data)


class KhlGameStatList(APIView):
    def get(self, request):
        khlgamestat = KhlGameStat.objects.all()
        data = KhlGameStatSerializer(khlgamestat, many=True).data
        return Response(data)


class KhlGameStatDetail(APIView):
    def get(self, request, pk):
        khlgamestat = get_object_or_404(KhlGameStat, pk=pk)
        data = KhlGameStatSerializer(khlgamestat).data
        return Response(data)


class TeamDetail(APIView):
    """ TODO Make qvery.
    def get(self, request, name):
        team = get_object_or_404(KhlTeam, name=name)
        data = KhlTeamSerializer(team).data
        return Response(data)"""
    pass