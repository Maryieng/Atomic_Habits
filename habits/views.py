from django.shortcuts import render
from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializers


class HabitCreateView(generics.CreateAPIView):
    """ создание привычки """
    serializer_class = HabitSerializers
    # permission_classes = [IsAuthenticated]


class HabitListView(generics.ListAPIView):
    """ список всех привычек """
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # pagination_class = WellAndLessonPagination


class HabitRetrieveView(generics.RetrieveAPIView):
    """ детальная информация привычки """
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsModerator, IsOwner]


class HabitUpdateView(generics.UpdateAPIView):
    """ изменение привычки """
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsModerator, IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    """ удаление привычки """
    queryset = Habit.objects.all()
    # permission_classes = [IsModerator, IsOwner]
