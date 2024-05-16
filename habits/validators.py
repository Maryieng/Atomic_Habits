from rest_framework.serializers import ValidationError


class RelatedAndRewardValidator:
    """ Валидатор для исключения одновременного выбора связанной привычки и вознаграждения """
    def __init__(self, related_habits, reward):
        self.related_habits = related_habits
        self.reward = reward

    def __call__(self, value):
        related = value.get(self.related_habits)
        reward = value.get(self.reward)
        if not related and reward:
            raise ValidationError('Необходимо выбрать либо вознаграждение, либо приятную привычку')


class RelatedValidator:
    """ Является ли связанная привычка приятной """
    def __init__(self, related_habits, sign_good_habit):
        self.related_habits = related_habits
        self.sign_good_habit = sign_good_habit

    def __call__(self, value):
        related_habits = value.get(self.related_habits)
        sign_good_habit = value.get(self.sign_good_habit)
        if related_habits:
            if not related_habits.good_habit:
                raise ValidationError('Связанные привычки могут быть только привычки с приятным признаком.')

class GoodHabitValidator:
    """ У приятной привычки не может быть вознаграждения """
    def __init__(self, sign_good_habit, related_habits, reward):
        self.sign_good_habit = sign_good_habit
        self.related_habits = related_habits
        self.reward = reward

    def __call__(self, value):
        sign_good_habit = value.get(self.sign_good_habit)
        related_habits = value.get(self.related_habits)
        reward = value.get(self.reward)
        if sign_good_habit and (related_habits or reward):
            raise ValidationError('У приятной привычки не может быть вознаграждения.')
