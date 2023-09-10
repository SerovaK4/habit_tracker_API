from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'place', 'time', 'action', 'is_pleasant_habit', 'frequency', 'reward', 'time_to_complete',
        'is_public', 'pleasant_habit',
    )
