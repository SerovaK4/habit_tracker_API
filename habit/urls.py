from django.urls import path

from habit.apps import HabitConfig
from rest_framework.routers import DefaultRouter

from habit.views import HabitCreateAPIView, HabitUpdateAPIView, HabitListView, HabitRetrieveAPIView, HabitDestroyAPIView

app_name = HabitConfig.name

router = DefaultRouter()


urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/', HabitListView.as_view(), name='habit-list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),

] + router.urls
