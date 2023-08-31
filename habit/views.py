from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habit.models import Habit
from habit.permissions import IsOwner
from habit.serializers import HabitCreateSerializer, HabitSerializers

'''


    Список привычек текущего пользователя с пагинацией
    Список публичных привычек
    Создание привычки
    Редактирование привычки
    Удаление привычки

'''

""" Создание привычки """


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    # pagination_class

    #def perform_create(self, serializer):
    #при создании - уведомление


""" Редактирование привычки """


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    pagination_class = [IsOwner, IsAuthenticated]


""" Список привычек текущего пользователя с пагинацией """


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    permission_class = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_class = [IsOwner, IsAuthenticated]


"""    Удаление привычки """


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_class = [IsOwner, IsAuthenticated]


""" Список публичных привычек """


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = [AllowAny]
