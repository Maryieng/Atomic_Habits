from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializers


class HabitCreateView(generics.CreateAPIView):
    """ создание привычки """
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]


class HabitListView(generics.ListAPIView):
    """ список всех привычек """
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        """ Пользователь видит только свои привычки """
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.filter(user=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class HabitRetrieveView(generics.RetrieveAPIView):
    """ детальная информация привычки """
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(generics.UpdateAPIView):
    """ изменение привычки """
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    """ удаление привычки """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
