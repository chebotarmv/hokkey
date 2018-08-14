# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class KhlTeam(models.Model):
    class Meta:
        verbose_name = 'Команда КХЛ'
        verbose_name_plural = 'Команды КХЛ'

    KHLTEAM = (
        ("Авангард", "Авангард"),
        ("Автомобилист", "Автомобилист"),
        ("Адмирал", "Адмирал"),
        ("Ак Барс", "Ак Барс"),
        ("Амур", "Амур"),
        ("Барыс", "Барыс"),
        ("Витязь", "Витязь"),
        ("Динамо Мн", "Динамо Мн"),
        ("Динамо Мск", "Динамо Мск"),
        ("Динамо Р", "Динамо Р"),
        ("Йокерит", "Йокерит"),
        ("Куньлунь РС", "Куньлунь РС"),
        ("Локомотив", "Локомотив"),
        ("Металлург Мг", "Металлург Мг"),
        ("Нефтехимик", "Нефтехимик"),
        ("Салават Юлаев", "Салават Юлаев"),
        ("Северсталь", "Северсталь"),
        ("Сибирь", "Сибирь"),
        ("СКА", "СКА"),
        ("Слован", "Слован"),
        ("ХК Сочи", "ХК Сочи"),
        ("Спартак", "Спартак"),
        ("Торпедо", "Торпедо"),
        ("Трактор", "Трактор"),
        ("ЦСКА", "ЦСКА"),
    )

    team_name = models.CharField('Имя команды',
                                 primary_key=True,
                                 max_length=50,
                                 blank=False,
                                 help_text="Choose team",
                                 choices=KHLTEAM)

    def __str__(self):
        return self.team_name


class KhlGameStat(models.Model):
    class Meta:
        verbose_name = 'Статистика по игре КХЛ'
        verbose_name_plural = 'Статистика по играм КХЛ'

    game_id = models.IntegerField(verbose_name='id игры', primary_key=True)
    first_team_name = models.ForeignKey(KhlTeam,
                                        verbose_name='Имя команы',
                                        related_name='first_team',
                                        to_field="team_name",
                                        on_delete=models.CASCADE)
    second_team_name = models.ForeignKey(KhlTeam,
                                         verbose_name='Имя команы',
                                         related_name='second_team',
                                         to_field="team_name",
                                         on_delete=models.CASCADE)
    fp_ft_shot = models.IntegerField('Броски по воротам первой команды в первом периоде', default=0)
    fp_ft_reflected = models.IntegerField('Отбитые броски первой команды в первом периоде', default=0)
    sp_ft_shot = models.IntegerField('Броски по воротам первой команды во втором периоде', default=0)
    sp_ft_reflected = models.IntegerField('Отбитые броски первой команды во втором периоде', default=0)
    tp_ft_shot = models.IntegerField('Броски по воротам первой команды в третьем периоде', default=0)
    tp_ft_reflected = models.IntegerField('Отбитые броски первой команды в третьем периоде', default=0)
    fp_st_shot = models.IntegerField('Броски по воротам второй команды в первом периоде', default=0)
    fp_st_reflected = models.IntegerField('Отбитые броски второй команды в первом периоде', default=0)
    sp_st_shot = models.IntegerField('Броски по воротам второй команды во втором периоде', default=0)
    sp_st_reflected = models.IntegerField('Отбитые броски второй команды во втором периоде', default=0)
    tp_st_shot = models.IntegerField('Броски по воротам третьей команды в третьем периоде', default=0)
    tp_st_reflected = models.IntegerField('Отбитые броски третьей команды в третьем периоде', default=0)
    game_data = models.DateField('Дата', default=date.today)


class NhlTeam(models.Model):
    class Meta:
        verbose_name = 'Команда НХЛ'
        verbose_name_plural = 'Команды НХЛ'

    NHLTEAM = (
        ("Айлендерс", "Айлендерс"),
        ("Анахайм Дакс", "Анахайм Дакс"),
        ("Аризона", "Аризона"),
        ("Баффало", "Баффало"),
        ("Бостон", "Бостон"),
        ("Ванкувер", "Ванкувер"),
        ("Вашингтон", "Вашингтон"),
        ("Вегас", "Вегас"),
        ("Виннипег", "Виннипег"),
        ("Даллас", "Даллас"),
        ("Детройт", "Детройт"),
        ("Калгари", "Калгари"),
        ("Каролина", "Каролина"),
        ("Коламбус", "Коламбус"),
        ("Колорадо", "Колорадо"),
        ("Лос-Анджелес", "Лос-Анджелес"),
        ("Миннесота", "Миннесота"),
        ("Монреаль", "Монреаль"),
        ("Нью-Джерси", "Нью-Джерси"),
        ("Нэшвилл", "Нэшвилл"),
        ("Оттава", "Оттава"),
        ("Пантерс", "Пантерс"),
        ("Питтсбург", "Питтсбург"),
        ("Рейнджерс", "Рейнджерс"),
        ("Сан-Хосе", "Сан-Хосе"),
        ("Тампа-Бэй", "Тампа-Бэй"),
        ("Торонто", "Торонто"),
        ("Филадельфия", "Филадельфия"),
        ("Чикаго", "Чикаго"),
        ("Эдмонтон", "Эдмонтон")
    )

    team_name = models.CharField('Имя команды',
                                 primary_key=True,
                                 max_length=50,
                                 blank=False,
                                 help_text="Choose team",
                                 choices=NHLTEAM)

    def __str__(self):
        return self.team_name


class NhlGameStat(models.Model):
    class Meta:
        verbose_name = 'Статистика по игре НХЛ'
        verbose_name_plural = 'Статистика по играм НХЛ'

    game_id = models.IntegerField(verbose_name='id игры', primary_key=True)
    first_team_name = models.ForeignKey(NhlTeam,
                                        verbose_name='Имя команы',
                                        related_name='first_team',
                                        to_field="team_name",
                                        on_delete=models.CASCADE)
    second_team_name = models.ForeignKey(NhlTeam,
                                         verbose_name='Имя команы',
                                         related_name='second_team',
                                         to_field="team_name",
                                         on_delete=models.CASCADE)
    fp_ft_shot = models.IntegerField('Броски по воротам первой команды в первом периоде', default=0)
    fp_ft_reflected = models.IntegerField('Отбитые броски первой команды в первом периоде', default=0)
    sp_ft_shot = models.IntegerField('Броски по воротам первой команды во втором периоде', default=0)
    sp_ft_reflected = models.IntegerField('Отбитые броски первой команды во втором периоде', default=0)
    tp_ft_shot = models.IntegerField('Броски по воротам первой команды в третьем периоде', default=0)
    tp_ft_reflected = models.IntegerField('Отбитые броски первой команды в третьем периоде', default=0)
    fp_st_shot = models.IntegerField('Броски по воротам второй команды в первом периоде', default=0)
    fp_st_reflected = models.IntegerField('Отбитые броски второй команды в первом периоде', default=0)
    sp_st_shot = models.IntegerField('Броски по воротам второй команды во втором периоде', default=0)
    sp_st_reflected = models.IntegerField('Отбитые броски второй команды во втором периоде', default=0)
    tp_st_shot = models.IntegerField('Броски по воротам третьей команды в третьем периоде', default=0)
    tp_st_reflected = models.IntegerField('Отбитые броски третьей команды в третьем периоде', default=0)
    game_data = models.DateField('Дата', default=date.today)
