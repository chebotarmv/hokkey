from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .views import get_last_five_khl_games_numbers, get_last_khl_game_numbers, get_all_khl_games_numbers, \
    get_last_nhl_game_numbers, get_last_five_nhl_games_numbers, get_all_nhl_games_numbers

from .models import KhlTeam, KhlGameStat, NhlTeam, NhlGameStat
from .serializers import KhlTeamSerializer, KhlGameStatSerializer, NhlTeamSerializer, NhlGameStatSerializer


class KhlTeamsList(APIView):
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


class LastKhlGameDetail(APIView):
    def get(self, request, name):
        data = get_last_khl_game_numbers(name)
        return Response(data)


class LastFiveKhlGamesDetail(APIView):
    def get(self, request, name):
        data = get_last_five_khl_games_numbers(name)
        return Response(data)


class AllKhlGamesDetail(APIView):
    def get(self, request, name):
        data = get_all_khl_games_numbers(name)
        return Response(data)


class NhlTeamsList(APIView):
    def get(self, request):
        teams = NhlTeam.objects.all()
        data = NhlTeamSerializer(teams, many=True).data
        return Response(data)


class NhlGameStatList(APIView):
    def get(self, request):
        nhlgamestat = NhlGameStat.objects.all()
        data = NhlGameStatSerializer(nhlgamestat, many=True).data
        return Response(data)


class NhlGameStatDetail(APIView):
    def get(self, request, pk):
        nhlgamestat = get_object_or_404(NhlGameStat, pk=pk)
        data = NhlGameStatSerializer(nhlgamestat).data
        return Response(data)


class LastNhlGameDetail(APIView):
    def get(self, request, name):
        data = get_last_nhl_game_numbers(name)
        return Response(data)


class LastFiveNhlGamesDetail(APIView):
    def get(self, request, name):
        data = get_last_five_nhl_games_numbers(name)
        return Response(data)


class AllNhlGamesDetail(APIView):
    def get(self, request, name):
        data = get_all_nhl_games_numbers(name)
        return Response(data)
