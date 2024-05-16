from rest_framework.serializers import ValidationError


class RelatedAndRewardValidator:
    """ Валидатор для исключения одновременного выбора связанной привычки и вознаграждения """
    def __init__(self, related, reward):
        self.related = related
        self.reward = reward

    def __call__(self, value):
        related = value.get(self.related)
        reward = value.get(self.reward)
        if not related and reward:
            raise ValidationError('Необходимо выбрать либо вознаграждение, либо приятную привычку')


class RelatedValidator:
    """ Является ли связанная привычка приятной """
    def __init__(self, related, sign_good_habit):
        self.related = related
        self.sign_good = sign_good_habit

    def __call__(self, value):
        related = value.get(self.related)
        sign_good = value.get(self.sign_good)
        if related:
            if not related.good_habit:
                raise ValidationError('Связанные привычки могут быть только привычки с приятным признаком.')

class GoodHabitValidator:
    """ У приятной привычки не может быть вознаграждения """
    def __init__(self, sign_good_habit, related, reward):
        self.sign_good_habit = sign_good_habit
        self.related = related
        self.reward = reward

    def __call__(self, value):
        sign_good_habit = value.get(self.sign_good_habit)
        related = value.get(self.related)
        reward = value.get(self.reward)
        if sign_good_habit and (related or reward):
            raise ValidationError('У приятной привычки не может быть вознаграждения.')
