from rest_framework.serializers import ValidationError


class PleasantValidator:
    def __init__(self, field):
        self.field = field

        """Невозможно Одновременно выбрать связанную привычку и приятную привычку."""

    def __call__(self, value):
        tmp_reward = dict(value).get('reward')
        tmp_is_related = dict(value).get('pleasant_habit')
        tmp_is_pleasant = dict(value).get('is_pleasant_habit')

        if tmp_is_pleasant and tmp_reward is not None:
            raise ValidationError('У приятной привычки не должно быть вознаграждения!')

        if tmp_is_pleasant and tmp_is_related is not None:
            raise ValidationError('Нельзя одновременно выбирать связанную и приятную привычку!')


class IsPleasantValidator:

    def __init__(self, fields):
        self.fields = fields

    """В связанные привычки могут попадать только привычки с признаком приятной привычки.."""

    def __call__(self, value):
        tmp_pleasant = dict(value).get(self.fields)
        if tmp_pleasant:
            if not tmp_pleasant.is_pleasant_habit:
                raise ValidationError('Возможно выбрать в связанную привычку только с признаком приятной привычки!')