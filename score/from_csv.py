import csv
import os
import sys

project_dir = '/home/mikhail/PycharmProjects/hokkey/sports'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from score.models import KhlGameStat
from score.models import KhlTeam
from datetime import datetime


def load_data(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in reversed(rows):
            p = KhlGameStat(first_team_name=KhlTeam(row['ft']), second_team_name=KhlTeam(row['st']),
                            fp_ft_shot=int(row['ftfps']), fp_ft_reflected=int(row['ftfpr']),
                            sp_ft_shot=int(row['ftsps']), sp_ft_reflected=int(row['ftspr']),
                            tp_ft_shot=int(row['fttps']), tp_ft_reflected=int(row['fttpr']),
                            fp_st_shot=int(row['stfps']), fp_st_reflected=int(row['stfpr']),
                            sp_st_shot=int(row['stsps']), sp_st_reflected=int(row['stspr']),
                            tp_st_shot=int(row['sttps']), tp_st_reflected=int(row['sttpr']),
                            game_data=datetime.strptime(row['data'], '%d.%m.%Y'))
            p.save()


if __name__ == '__main__':
    print("Starting script...")

    load_data('/home/mikhail/PycharmProjects/hokk/result_2.csv')
