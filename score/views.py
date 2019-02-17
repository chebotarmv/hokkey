# -*- coding: utf-8 -*-
from .models import KhlTeam, NhlTeam, KhlGameStat, NhlGameStat
from django.http import HttpResponseRedirect
from django.shortcuts import render
from score.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def home_page(request):
    khldata = KhlGameStat.objects.all().values().order_by('-game_id')[:5]
    nhldata = NhlGameStat.objects.all().values().order_by('-game_id')[:5]
    return render(request, 'score/home_page.html', context={'khldata': khldata, 'nhldata': nhldata})


def khl(request):
    khl_teams = KhlTeam.objects.all()
    return render(request, 'score/khl_page.html', {'khl_teams': khl_teams})


def nhl(request):
    nhl_teams = NhlTeam.objects.all()
    return render(request, 'score/nhl_page.html', {'nhl_teams': nhl_teams})


def khl_archive(request):
    data = KhlGameStat.objects.all().values().order_by('-game_id')
    return render(request, 'score/khl_archive.html', context={'data': data})


def nhl_archive(request):
    data = NhlGameStat.objects.all().values().order_by('-game_id')
    return render(request, 'score/nhl_archive.html', context={'data': data})

@login_required
@permission_required('score.add_khlgamestat')
def makekhldata(request):
    if request.method == 'POST':
        khlform = KhlGameStatForm(request.POST)
        if khlform.is_valid():
            khl = khlform.save(commit=False)
            khl.id = len(KhlGameStat.objects.all()) + 1
            khl.save()
        return HttpResponseRedirect('/thanks/')
    else:
        khlform = KhlGameStatForm()
    return render(request, "score/make_khl_data.html", {'form': khlform})

@login_required
@permission_required('score.add_nhlgamestat')
def makenhldata(request):
    if request.method == 'POST':
        nhlform = NhlGameStatForm(request.POST)
        if nhlform.is_valid():
            nhl = nhlform.save(commit=False)
            nhl.id = len(NhlGameStat.objects.all()) + 1
            nhl.save()
        return HttpResponseRedirect('/thanks/')
    else:
        nhlform = NhlGameStatForm()
    return render(request, "score/make_nhl_data.html", {'form': nhlform})


def thanks(request):
    return render(request, 'score/thanks.html', {})


def khlteamstat(request, name):
    def get_last_game_numbers(name):
        last_game_context = {}
        games = KhlGameStat.objects.filter(first_team_name_id=name).order_by('-game_data') | \
                KhlGameStat.objects.filter(second_team_name_id=name).order_by('-game_data')
        last_game = games[:1].values()
        last_game = last_game[0]
        if last_game['first_team_name_id'] == name:
            team = last_game['first_team_name_id']
            last_game_context['team'] = team
            fp_ft_shot = last_game['fp_ft_shot']
            last_game_context['fp_ft_shot'] = fp_ft_shot
            fp_ft_reflected = last_game['fp_ft_reflected']
            last_game_context['fp_ft_reflected'] = fp_ft_reflected
            sp_ft_shot = last_game['sp_ft_shot']
            last_game_context['sp_ft_shot'] = sp_ft_shot
            sp_ft_reflected = last_game['sp_ft_reflected']
            last_game_context['sp_ft_reflected'] = sp_ft_reflected
            tp_ft_shot = last_game['tp_ft_shot']
            last_game_context['tp_ft_shot'] = tp_ft_shot
            tp_ft_reflected = last_game['tp_ft_reflected']
            last_game_context['tp_ft_reflected'] = tp_ft_reflected
            game_data = last_game['game_data']
            last_game_context['game_data'] = game_data
            return last_game_context
        else:
            team = last_game['first_team_name_id']
            last_game_context['team'] = team
            fp_st_shot = last_game['fp_ft_shot']
            last_game_context['fp_ft_shot'] = fp_st_shot
            fp_st_reflected = last_game['fp_ft_reflected']
            last_game_context['fp_ft_reflected'] = fp_st_reflected
            sp_st_shot = last_game['sp_ft_shot']
            last_game_context['sp_ft_shot'] = sp_st_shot
            sp_st_reflected = last_game['sp_ft_reflected']
            last_game_context['sp_ft_reflected'] = sp_st_reflected
            tp_st_shot = last_game['tp_ft_shot']
            last_game_context['tp_ft_shot'] = tp_st_shot
            tp_st_reflected = last_game['tp_ft_reflected']
            last_game_context['tp_ft_reflected'] = tp_st_reflected
            game_data = last_game['game_data']
            last_game_context['game_data'] = game_data
            return last_game_context

    def get_last_five_games_numbers(name):
        last_five_games_context = {}
        games = KhlGameStat.objects.filter(first_team_name_id=name).order_by('-game_data') | \
                KhlGameStat.objects.filter(second_team_name_id=name).order_by('-game_data')
        last_five_games = games[:5].values()
        shots_in_first_period = []
        reflected_in_first_period = []
        shots_in_second_period = []
        reflected_in_second_period = []
        shots_in_third_period = []
        reflected_in_third_period = []
        for game in last_five_games:
            if game['first_team_name_id'] == name:
                fp_ft_shot = game['fp_ft_shot']
                fp_ft_reflected = game['fp_ft_reflected']
                sp_ft_shot = game['sp_ft_shot']
                sp_ft_reflected = game['sp_ft_reflected']
                tp_ft_shot = game['tp_ft_shot']
                tp_ft_reflected = game['tp_ft_reflected']
                shots_in_first_period.append(int(fp_ft_shot))
                reflected_in_first_period.append(int(fp_ft_reflected))
                shots_in_second_period.append(int(sp_ft_shot))
                reflected_in_second_period.append(int(sp_ft_reflected))
                shots_in_third_period.append(int(tp_ft_shot))
                reflected_in_third_period.append(int(tp_ft_reflected))
            else:
                fp_st_shot = game['fp_st_shot']
                fp_st_reflected = game['fp_st_reflected']
                sp_st_shot = game['sp_st_shot']
                sp_st_reflected = game['sp_st_reflected']
                tp_st_shot = game['tp_st_shot']
                tp_st_reflected = game['tp_st_reflected']
                shots_in_first_period.append(int(fp_st_shot))
                reflected_in_first_period.append(int(fp_st_reflected))
                shots_in_second_period.append(int(sp_st_shot))
                reflected_in_second_period.append(int(sp_st_reflected))
                shots_in_third_period.append(int(tp_st_shot))
                reflected_in_third_period.append(int(tp_st_reflected))
        shots_in_first_period = sum(shots_in_first_period) // len(shots_in_first_period)
        last_five_games_context['shots_in_first_period'] = shots_in_first_period
        reflected_in_first_period = sum(reflected_in_first_period) // len(reflected_in_first_period)
        last_five_games_context['reflected_in_first_period'] = reflected_in_first_period
        shots_in_second_period = sum(shots_in_second_period) // len(shots_in_second_period)
        last_five_games_context['shots_in_second_period'] = shots_in_second_period
        reflected_in_second_period = sum(reflected_in_second_period) // len(reflected_in_second_period)
        last_five_games_context['reflected_in_second_period'] = reflected_in_second_period
        shots_in_third_period = sum(shots_in_third_period) // len(shots_in_third_period)
        last_five_games_context['shots_in_third_period'] = shots_in_third_period
        reflected_in_third_period = sum(reflected_in_third_period) // len(reflected_in_third_period)
        last_five_games_context['reflected_in_third_period'] = reflected_in_third_period
        return last_five_games_context

    def get_all_games_numbers(name):
        all_games_context = {}
        games = KhlGameStat.objects.filter(first_team_name_id=name).order_by('-game_data') | \
                KhlGameStat.objects.filter(second_team_name_id=name).order_by('-game_data')
        all_games = games.values()
        shots_in_first_period_all_games = []
        reflected_in_first_period_all_games = []
        shots_in_second_period_all_games = []
        reflected_in_second_period_all_games = []
        shots_in_third_period_all_games = []
        reflected_in_third_period_all_games = []
        for game in all_games:
            if game['first_team_name_id'] == name:
                fp_ft_shot = game['fp_ft_shot']
                fp_ft_reflected = game['fp_ft_reflected']
                sp_ft_shot = game['sp_ft_shot']
                sp_ft_reflected = game['sp_ft_reflected']
                tp_ft_shot = game['tp_ft_shot']
                tp_ft_reflected = game['tp_ft_reflected']
                shots_in_first_period_all_games.append(int(fp_ft_shot))
                reflected_in_first_period_all_games.append(int(fp_ft_reflected))
                shots_in_second_period_all_games.append(int(sp_ft_shot))
                reflected_in_second_period_all_games.append(int(sp_ft_reflected))
                shots_in_third_period_all_games.append(int(tp_ft_shot))
                reflected_in_third_period_all_games.append(int(tp_ft_reflected))
            else:
                fp_st_shot = game['fp_st_shot']
                fp_st_reflected = game['fp_st_reflected']
                sp_st_shot = game['sp_st_shot']
                sp_st_reflected = game['sp_st_reflected']
                tp_st_shot = game['tp_st_shot']
                tp_st_reflected = game['tp_st_reflected']
                shots_in_first_period_all_games.append(int(fp_st_shot))
                reflected_in_first_period_all_games.append(int(fp_st_reflected))
                shots_in_second_period_all_games.append(int(sp_st_shot))
                reflected_in_second_period_all_games.append(int(sp_st_reflected))
                shots_in_third_period_all_games.append(int(tp_st_shot))
                reflected_in_third_period_all_games.append(int(tp_st_reflected))
        shots_in_first_period_all_games = sum(shots_in_first_period_all_games) // \
                                          len(shots_in_first_period_all_games)
        all_games_context['shots_in_first_period_all_games'] = shots_in_first_period_all_games
        reflected_in_first_period_all_games = sum(reflected_in_first_period_all_games) // \
                                              len(reflected_in_first_period_all_games)
        all_games_context['reflected_in_first_period_all_games'] = reflected_in_first_period_all_games
        shots_in_second_period_all_games = sum(shots_in_second_period_all_games) // \
                                           len(shots_in_second_period_all_games)
        all_games_context['shots_in_second_period_all_games'] = shots_in_second_period_all_games
        reflected_in_second_period_all_games = sum(reflected_in_second_period_all_games) // \
                                               len(reflected_in_second_period_all_games)
        all_games_context['reflected_in_second_period_all_games'] = reflected_in_second_period_all_games
        shots_in_third_period_all_games = sum(shots_in_third_period_all_games) // \
                                          len(shots_in_third_period_all_games)
        all_games_context['shots_in_third_period_all_games'] = shots_in_third_period_all_games
        reflected_in_third_period_all_games = sum(reflected_in_third_period_all_games) // \
                                              len(reflected_in_third_period_all_games)
        all_games_context['reflected_in_third_period_all_games'] = reflected_in_third_period_all_games
        return all_games_context
    context = {**get_last_game_numbers(name), **get_last_five_games_numbers(name), **get_all_games_numbers(name)}
    return render(request, 'score/khlteamstat.html', context)


def nhlteamstat(request, name):
    def get_last_game_numbers(name):
        last_game_context = {}
        games = NhlGameStat.objects.filter(first_team_name_id=name).order_by('-game_data') | \
                NhlGameStat.objects.filter(second_team_name_id=name).order_by('-game_data')
        last_game = games[:1].values()
        last_game = last_game[0]
        if last_game['first_team_name_id'] == name:
            team = last_game['first_team_name_id']
            last_game_context['team'] = team
            fp_ft_shot = last_game['fp_ft_shot']
            last_game_context['fp_ft_shot'] = fp_ft_shot
            fp_ft_reflected = last_game['fp_ft_reflected']
            last_game_context['fp_ft_reflected'] = fp_ft_reflected
            sp_ft_shot = last_game['sp_ft_shot']
            last_game_context['sp_ft_shot'] = sp_ft_shot
            sp_ft_reflected = last_game['sp_ft_reflected']
            last_game_context['sp_ft_reflected'] = sp_ft_reflected
            tp_ft_shot = last_game['tp_ft_shot']
            last_game_context['tp_ft_shot'] = tp_ft_shot
            tp_ft_reflected = last_game['tp_ft_reflected']
            last_game_context['tp_ft_reflected'] = tp_ft_reflected
            game_data = last_game['game_data']
            last_game_context['game_data'] = game_data
            return last_game_context
        else:
            team = last_game['first_team_name_id']
            last_game_context['team'] = team
            fp_st_shot = last_game['fp_ft_shot']
            last_game_context['fp_ft_shot'] = fp_st_shot
            fp_st_reflected = last_game['fp_ft_reflected']
            last_game_context['fp_ft_reflected'] = fp_st_reflected
            sp_st_shot = last_game['sp_ft_shot']
            last_game_context['sp_ft_shot'] = sp_st_shot
            sp_st_reflected = last_game['sp_ft_reflected']
            last_game_context['sp_ft_reflected'] = sp_st_reflected
            tp_st_shot = last_game['tp_ft_shot']
            last_game_context['tp_ft_shot'] = tp_st_shot
            tp_st_reflected = last_game['tp_ft_reflected']
            last_game_context['tp_ft_reflected'] = tp_st_reflected
            game_data = last_game['game_data']
            last_game_context['game_data'] = game_data
            return last_game_context

    def get_last_five_games_numbers(name):
        last_five_games_context = {}
        games = NhlGameStat.objects.filter(first_team_name_id=name).order_by('-game_data') | \
                NhlGameStat.objects.filter(second_team_name_id=name).order_by('-game_data')
        last_five_games = games[:5].values()
        shots_in_first_period = []
        reflected_in_first_period = []
        shots_in_second_period = []
        reflected_in_second_period = []
        shots_in_third_period = []
        reflected_in_third_period = []
        for game in last_five_games:
            if game['first_team_name_id'] == name:
                fp_ft_shot = game['fp_ft_shot']
                fp_ft_reflected = game['fp_ft_reflected']
                sp_ft_shot = game['sp_ft_shot']
                sp_ft_reflected = game['sp_ft_reflected']
                tp_ft_shot = game['tp_ft_shot']
                tp_ft_reflected = game['tp_ft_reflected']
                shots_in_first_period.append(int(fp_ft_shot))
                reflected_in_first_period.append(int(fp_ft_reflected))
                shots_in_second_period.append(int(sp_ft_shot))
                reflected_in_second_period.append(int(sp_ft_reflected))
                shots_in_third_period.append(int(tp_ft_shot))
                reflected_in_third_period.append(int(tp_ft_reflected))
            else:
                fp_st_shot = game['fp_st_shot']
                fp_st_reflected = game['fp_st_reflected']
                sp_st_shot = game['sp_st_shot']
                sp_st_reflected = game['sp_st_reflected']
                tp_st_shot = game['tp_st_shot']
                tp_st_reflected = game['tp_st_reflected']
                shots_in_first_period.append(int(fp_st_shot))
                reflected_in_first_period.append(int(fp_st_reflected))
                shots_in_second_period.append(int(sp_st_shot))
                reflected_in_second_period.append(int(sp_st_reflected))
                shots_in_third_period.append(int(tp_st_shot))
                reflected_in_third_period.append(int(tp_st_reflected))
        shots_in_first_period = sum(shots_in_first_period) // len(shots_in_first_period)
        last_five_games_context['shots_in_first_period'] = shots_in_first_period
        reflected_in_first_period = sum(reflected_in_first_period) // len(reflected_in_first_period)
        last_five_games_context['reflected_in_first_period'] = reflected_in_first_period
        shots_in_second_period = sum(shots_in_second_period) // len(shots_in_second_period)
        last_five_games_context['shots_in_second_period'] = shots_in_second_period
        reflected_in_second_period = sum(reflected_in_second_period) // len(reflected_in_second_period)
        last_five_games_context['reflected_in_second_period'] = reflected_in_second_period
        shots_in_third_period = sum(shots_in_third_period) // len(shots_in_third_period)
        last_five_games_context['shots_in_third_period'] = shots_in_third_period
        reflected_in_third_period = sum(reflected_in_third_period) // len(reflected_in_third_period)
        last_five_games_context['reflected_in_third_period'] = reflected_in_third_period
        return last_five_games_context

    def get_all_games_numbers(name):
        all_games_context = {}
        games = NhlGameStat.objects.filter(first_team_name_id=name).order_by('-game_data') | \
                NhlGameStat.objects.filter(second_team_name_id=name).order_by('-game_data')
        all_games = games.values()
        shots_in_first_period_all_games = []
        reflected_in_first_period_all_games = []
        shots_in_second_period_all_games = []
        reflected_in_second_period_all_games = []
        shots_in_third_period_all_games = []
        reflected_in_third_period_all_games = []
        for game in all_games:
            if game['first_team_name_id'] == name:
                fp_ft_shot = game['fp_ft_shot']
                fp_ft_reflected = game['fp_ft_reflected']
                sp_ft_shot = game['sp_ft_shot']
                sp_ft_reflected = game['sp_ft_reflected']
                tp_ft_shot = game['tp_ft_shot']
                tp_ft_reflected = game['tp_ft_reflected']
                shots_in_first_period_all_games.append(int(fp_ft_shot))
                reflected_in_first_period_all_games.append(int(fp_ft_reflected))
                shots_in_second_period_all_games.append(int(sp_ft_shot))
                reflected_in_second_period_all_games.append(int(sp_ft_reflected))
                shots_in_third_period_all_games.append(int(tp_ft_shot))
                reflected_in_third_period_all_games.append(int(tp_ft_reflected))
            else:
                fp_st_shot = game['fp_st_shot']
                fp_st_reflected = game['fp_st_reflected']
                sp_st_shot = game['sp_st_shot']
                sp_st_reflected = game['sp_st_reflected']
                tp_st_shot = game['tp_st_shot']
                tp_st_reflected = game['tp_st_reflected']
                shots_in_first_period_all_games.append(int(fp_st_shot))
                reflected_in_first_period_all_games.append(int(fp_st_reflected))
                shots_in_second_period_all_games.append(int(sp_st_shot))
                reflected_in_second_period_all_games.append(int(sp_st_reflected))
                shots_in_third_period_all_games.append(int(tp_st_shot))
                reflected_in_third_period_all_games.append(int(tp_st_reflected))
        shots_in_first_period_all_games = sum(shots_in_first_period_all_games) // \
                                          len(shots_in_first_period_all_games)
        all_games_context['shots_in_first_period_all_games'] = shots_in_first_period_all_games
        reflected_in_first_period_all_games = sum(reflected_in_first_period_all_games) // \
                                              len(reflected_in_first_period_all_games)
        all_games_context['reflected_in_first_period_all_games'] = reflected_in_first_period_all_games
        shots_in_second_period_all_games = sum(shots_in_second_period_all_games) // \
                                           len(shots_in_second_period_all_games)
        all_games_context['shots_in_second_period_all_games'] = shots_in_second_period_all_games
        reflected_in_second_period_all_games = sum(reflected_in_second_period_all_games) // \
                                               len(reflected_in_second_period_all_games)
        all_games_context['reflected_in_second_period_all_games'] = reflected_in_second_period_all_games
        shots_in_third_period_all_games = sum(shots_in_third_period_all_games) // \
                                          len(shots_in_third_period_all_games)
        all_games_context['shots_in_third_period_all_games'] = shots_in_third_period_all_games
        reflected_in_third_period_all_games = sum(reflected_in_third_period_all_games) // \
                                              len(reflected_in_third_period_all_games)
        all_games_context['reflected_in_third_period_all_games'] = reflected_in_third_period_all_games
        return all_games_context
    context = {**get_last_game_numbers(name), **get_last_five_games_numbers(name), **get_all_games_numbers(name)}
    return render(request, 'score/nhlteamstat.html', context)
