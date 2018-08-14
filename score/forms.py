from django.forms import ModelForm, SelectDateWidget
from score.models import KhlGameStat
from score.models import NhlGameStat

class KhlGameStatForm(ModelForm):
    class Meta:
        model = KhlGameStat
        fields = ['first_team_name', 'second_team_name', 'fp_ft_shot', 'fp_ft_reflected', 'sp_ft_shot',
                  'sp_ft_reflected', 'tp_ft_shot', 'tp_ft_reflected', 'fp_st_shot', 'fp_st_reflected', 'sp_st_shot',
                  'sp_st_reflected', 'tp_st_shot', 'tp_st_reflected', 'game_data']
        widgets = {'game_data': SelectDateWidget()}

class NhlGameStatForm(ModelForm):
    class Meta:
        model = NhlGameStat
        fields = ['first_team_name', 'second_team_name', 'fp_ft_shot', 'fp_ft_reflected', 'sp_ft_shot',
                  'sp_ft_reflected', 'tp_ft_shot', 'tp_ft_reflected', 'fp_st_shot', 'fp_st_reflected', 'sp_st_shot',
                  'sp_st_reflected', 'tp_st_shot', 'tp_st_reflected', 'game_data']
        widgets = {'game_data': SelectDateWidget()}