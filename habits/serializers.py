from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedAndRewardValidator, RelatedValidator, GoodHabitValidator


class HabitSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели Привычек """

    class Meta:
        model = Habit
        fields = '__all__'

    validators = [
        RelatedAndRewardValidator(related_habits='related_habits', reward='reward'),
        RelatedValidator(related_habits='related_habits', sign_good_habit='sign_good_habit'),
        GoodHabitValidator(sign_good_habit='sign_good_habit', related_habits='related_habits', reward='reward')
    ]
