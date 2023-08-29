from rest_framework import serializers

from habit.models import Habit


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'user', 'place', 'time', 'action', 'is_pleasant', 'frequency', 'reward', 'time_to_complete', 'is_public')


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        # validators
