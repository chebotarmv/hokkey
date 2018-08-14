from django.contrib import admin
from .models import KhlTeam, KhlGameStat, NhlTeam, NhlGameStat

admin.site.register(KhlTeam)
admin.site.register(KhlGameStat)
admin.site.register(NhlTeam)
admin.site.register(NhlGameStat)