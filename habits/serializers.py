from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedAndRewardValidator, RelatedValidator, GoodHabitValidator


class HabitSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели Привычек """

    class Meta:
        model = Habit
        fields = '__all__'

    validators = [
        RelatedAndRewardValidator(related='related', reward='reward'),
        RelatedValidator(related='related', sign_good_habit='sign_good_habit'),
        GoodHabitValidator(sign_good_habit='sign_good_habit', related='related', reward='reward')
    ]
