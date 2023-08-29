from rest_framework import viewsets, generics

from habit.models import Habit
from habit.serializers import HabitCreateSerializer, HabitSerializers

'''


    Список привычек текущего пользователя с пагинацией
    Список публичных привычек
    Создание привычки
    Редактирование привычки
    Удаление привычки

'''

"""
    Создание привычки
"""


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    queryset = Habit.objects.all()
    # permission_classes
    # pagination_class


"""
    Редактирование привычки
"""


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()


"""
    Список привычек текущего пользователя с пагинацией/     Список публичных привычек
"""


class HabitListView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()


"""
    Удаление привычки
"""


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
