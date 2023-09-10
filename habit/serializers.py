from rest_framework import serializers

from habit.models import Habit
from habit.validators import IsPleasantValidator, PleasantValidator, TimePleasantValidator


class PleasureHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('user', 'place', 'time', 'action', 'pleasant_habit', 'frequency', 'time_to_complete', 'is_public',
                  'pleasant_habit')


class HabitSerializers(serializers.ModelSerializer):
    pleasant_habit = PleasureHabitSerializer(source='habit', many=True)

    class Meta:
        model = Habit
        fields = "__all__"


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id', 'user', 'place', 'time', 'action', 'is_pleasant_habit', 'frequency', 'reward', 'time_to_complete',
            'is_public', 'pleasant_habit')
        validators = [PleasantValidator(fields), IsPleasantValidator(fields='pleasant_habit'),
                      TimePleasantValidator(fields='time_to_complete')]
