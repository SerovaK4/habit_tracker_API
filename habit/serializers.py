from rest_framework import serializers

from habit.models import Habit
from habit.validators import IsPleasantValidator, PleasantValidator


class PleasureHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('user', 'place', 'time', 'action', 'pleasant_habit', 'frequency', 'time_to_complete', 'is_public')


class HabitSerializers(serializers.ModelSerializer):
    pleasant_habit = PleasureHabitSerializer(source='habit', many=True)

    class Meta:
        model = Habit
        fields = (
            'user', 'place', 'time', 'action', 'is_pleasant', 'frequency', 'reward', 'time_to_complete', 'is_public')


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [PleasantValidator(fields), IsPleasantValidator(fields='pleasant_habit')]
