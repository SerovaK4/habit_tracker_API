from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from habit.models import Habit
from users.models import User

from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User

class MyAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Авторизуем пользователя с помощью `client.force_authenticate()`
        self.client.force_authenticate(user=self.user)
        # Получаем URL для обращения к API
        self.url = reverse('my-model-list-api')
    def test_api_view_without_authentication(self):
        # Отключаем аутентификацию для тестирования
        self.client.force_authenticate(user=None)

        # Запрос без авторизации
        response = self.client.get('/my-api/')
        self.assertEqual(response.status_code, 200)

    def test_api_view_with_authentication(self):
        # Имитация аутентифицированного пользователя
        self.client.force_authenticate(user=self.user)

        # Запрос с авторизацией
        response = self.client.get('/my-api/')
        self.assertEqual(response.status_code, 200)

    def test_create_habit(self):
        habit_1 = Habit.objects.create(
            user=self.user,
            place='testing room',
            time='8:00:00',
            action='testing',
            is_pleasant_habit=False,
            frequency='1',
            reward=None,
            pleasant_habit=None,
            is_public=True,

        )
        response = self.client.post(self.url, habit_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
