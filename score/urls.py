# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
from .apiviews import KhlTeamsList, KhlGameStatList, KhlGameStatDetail, LastKhlGameDetail, LastFiveKhlGamesDetail, \
    AllKhlGamesDetail, NhlTeamsList, NhlGameStatList, NhlGameStatDetail, LastNhlGameDetail, LastFiveNhlGamesDetail, \
    AllNhlGamesDetail

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('khl/', views.khl, name='khl'),
    path('nhl/', views.nhl, name='nhl'),
    path('khl/<name>/', views.khlteamstat, name='khl_team'),
    path('nhl/<name>/', views.nhlteamstat, name='nhl_team'),
    path('thanks', views.thanks, name='thanks'),
    path('archivekhl', views.khl_archive, name='khl_archive'),
    path('archivenhl', views.nhl_archive, name='nhl_archive'),
    path('makekhldata', views.makekhldata, name='make_khl_data'),
    path('makenhldata', views.makenhldata, name='make_nhl_data'),

    path('api/khl_teams', KhlTeamsList.as_view(), name='khl_teams_list'),
    path('api/khl_games', KhlGameStatList.as_view(), name='khl_games_list'),
    path('api/khl_games/<int:pk>/', KhlGameStatDetail.as_view(), name='khl_game_detail'),
    path('api/khl_games/last_game/<name>', LastKhlGameDetail.as_view(), name='khl_last_game'),
    path('api/khl_games/last_five_games/<name>', LastFiveKhlGamesDetail.as_view(), name='khl_last_five_game'),
    path('api/khl_games/all_games/<name>', AllKhlGamesDetail.as_view(), name='khl_last_five_game'),

    path('api/nhl_teams', NhlTeamsList.as_view(), name='nhl_teams_list'),
    path('api/nhl_games', NhlGameStatList.as_view(), name='nhl_games_list'),
    path('api/nhl_games/<int:pk>/', NhlGameStatDetail.as_view(), name='nhl_game_detail'),
    path('api/nhl_games/last_game/<name>', LastNhlGameDetail.as_view(), name='nhl_last_game'),
    path('api/nhl_games/last_five_games/<name>', LastFiveNhlGamesDetail.as_view(), name='nhl_last_five_game'),
    path('api/nhl_games/all_games/<name>', AllNhlGamesDetail.as_view(), name='nhl_last_five_game'),

    path(r'swagger-docs/', schema_view),
]