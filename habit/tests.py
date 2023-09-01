from rest_framework.test import APITestCase
from rest_framework import status

from habit.models import Habit
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.url = '/v1/habit/'

        self.user = User.objects.create(
            email='test_1@sky.pro',
            chat_id=12345,
        )
        self.user.set_password('test123')
        self.user.save()

        self.user_2 = User.objects.create(
            email='test_2@sky.pro',
            chat_id=12345,
        )
        self.user_2.set_password('test321')
        self.user_2.save()

        self.user_without_tg_chat_id = User.objects.create(
            email='without_tg_chat@sky.pro',
        )

        self.user_2.set_password("test321")
        self.user_2.save()

        self.habit_1 = Habit.objects.create(
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

        self.habit_2 = Habit.objects.create(
            user=self.user_2,
            place='testing room 2',
            time='16:00:00',
            action='testing',
            is_pleasant_habit=False,
            frequency='1',
            reward=None,
            pleasant_habit=None,
            is_public=False,

        )

        self.habit_3 = Habit.objects.create(
            user=self.user_2,
            place='testing room 2',
            time='16:00:00',
            action='testing',
            is_pleasant_habit=True,
            frequency='1',
            is_public=True,

        )



    def test_create_habit(self):
        habit_1 = {
            "user": self.user_2,
            "place": 'testing room 2',
            "time": '16:00:00',
            "action": 'testing',
            "is_pleasant_habit": True,
            "frequency": '1',
            "is_public": True,
        }
        response = self.client.post(
            urls="habit/",
            data=habit_1
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_list(self):
        """Тестирование вывода списка привычек"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            'habit/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
