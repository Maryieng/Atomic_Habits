from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_linked_habit, validate_reward_for_useful_habit, validate_related_or_reward, \
    validate_only_include_sign_good_habit


class HabitSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели Привычек """

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """ Валидаторы для проверок по условиям """
        habit = Habit(**data)

        validate_linked_habit(habit)
        validate_reward_for_useful_habit(habit)
        validate_related_or_reward(habit)
        validate_only_include_sign_good_habit(habit)
        return data
