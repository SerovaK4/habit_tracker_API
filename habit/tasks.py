from datetime import datetime

from celery import shared_task
from telebot import TeleBot

from config import settings
from habit.models import Habit

""" Отправка сообщения в телеграме"""


@shared_task
def notification_bot():
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time == datetime.now():
            bot = TeleBot(settings.TELEGRAM_BOT_API_KEY)
            message = f"Трекер привычек напоминает вам о необходимости выполнить {habit.action} в {habit.time} в {habit.place}"
            bot.send_message(habit.user.chat_id, message)
