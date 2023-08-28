from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True
}


class Habit(models.Model):

    """класс описывающий атомные привычки"""

    EXECUTION_FREQUENCY = [
        (1, "Один раз в неделю"),
        (2, "Два раза в неделю"),
        (3, "Три раза в неделю"),
        (4, "Четыре раза в неделю"),
        (5, "Пять раз в неделю"),
        (6, "Шесть раз в неделю"),
        (7, "Каждый день"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь') #создатель привычки
    place = models.CharField(max_length=150, verbose_name="Место") #место, в котором необходимо выполнять привычку
    time = models.DateTimeField(default=datetime.now(), verbose_name="Время")#время, когда необходимо выполнять привычку
    action = models.CharField(max_length=250, verbose_name="Действие") #действие, которое представляет из себя привычка
    is_pleasant = models.BooleanField(default=False, verbose_name="Признак приятной привычки", **NULLABLE) #привычка, которую можно привязать к выполнению полезной привычки
    #related_habit = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Связанная привычка', **NULLABLE) #привычка, которая связана с другой привычкой
    frequency = models.PositiveIntegerField(choices=EXECUTION_FREQUENCY, default=1, verbose_name="Периодичность") #периодичность выполнения привычки для напоминания в днях
    reward = models.CharField(max_length=250, verbose_name="Вознаграждение", **NULLABLE) #то, чем пользователь должен себя вознаградить после выполнения
    time_to_complete = models.PositiveIntegerField(default=0, verbose_name="Время на выполнение", validators=[MaxValueValidator(120)]) # время, которое предположительно потратит пользователь на выполнение привычки
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности") #возможность публиковать привычки в общий доступ

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
