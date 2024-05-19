from rest_framework.serializers import ValidationError


def validate_related_or_reward(habit):
    if not habit.related and habit.reward:
        raise ValidationError('Необходимо выбрать либо вознаграждение, либо приятную привычку')


def validate_linked_habit(habit):
    if habit.sign_good_habit and (habit.related or habit.reward) is not None:
        raise ValidationError('Приятные привычки не могут иметь связанную привычку')


def validate_reward_for_useful_habit(habit):
    if not habit.sign_good_habit and habit.reward:
        raise ValidationError('Только полезные привычки могут иметь награду')


def validate_only_include_sign_good_habit(habit):
    if habit.related and not habit.sign_good_habit:
        raise ValidationError('Связанной привычкой может быть только приятная привычка')
