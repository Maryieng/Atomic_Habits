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


class GetPublicHabitListView(generics.ListAPIView):
    """ Посмотр списка всех публичных привычек """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializers
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]


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
