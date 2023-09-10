from django.utils import timezone

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=150, verbose_name="Место")
    time = models.DateTimeField(default=timezone.now, verbose_name="Время")
    action = models.CharField(max_length=250, verbose_name="Действие")
    pleasant_habit = models.ForeignKey('self', verbose_name='Приятная привычка', on_delete=models.CASCADE, **NULLABLE, related_name='habit')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки", **NULLABLE)
    frequency = models.PositiveIntegerField(choices=EXECUTION_FREQUENCY, default=1, verbose_name="Периодичность")
    reward = models.CharField(max_length=250, verbose_name="Вознаграждение", **NULLABLE)
    time_to_complete = models.TimeField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
