# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home_page, name='home_page'),
    url(r'khl/(\D+)/', views.khlteamstat, name='khl_team'),
    url(r'nhl/(\D+)/', views.nhlteamstat, name='nhl_team'),
    url(r'khl$', views.khl, name='khl'),
    url(r'nhl$', views.nhl, name='nhl'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^archivekhl', views.khl_archive, name='khl_archive'),
    url(r'^archivenhl', views.nhl_archive, name='nhl_archive'),
    url(r'^makekhldata', views.makekhldata, name='make_khl_data'),
    url(r'^makenhldata', views.makenhldata, name='make_nhl_data'),
]