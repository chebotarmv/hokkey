# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .apiviews import TeamsList, KhlGameStatList, KhlGameStatDetail

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
    path('api/teams', TeamsList.as_view(), name='teams_list'),
    path('api/games', KhlGameStatList.as_view(), name='games_list'),
    path('api/games/<int:pk>/', KhlGameStatDetail.as_view(), name='games_list'),
]