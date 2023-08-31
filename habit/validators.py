from django.core.exceptions import ValidationError
from models import Habit

class PleasantValidator:
    """Невозможно Одновременно выбрать связанную привычку и приятную привычку."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pass