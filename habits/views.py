from django.shortcuts import render
from rest_framework import generics

from habits.models import Habit


class LessonCreateView(generics.CreateAPIView):
    """ создание привычки """
    # serializer_class =
    # permission_classes = [IsAuthenticated]


class LessonListView(generics.ListAPIView):
    """ список всех привычек """
    # serializer_class =
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # pagination_class = WellAndLessonPagination


class LessonRetrieveView(generics.RetrieveAPIView):
    """ детальная информация привычки """
    # serializer_class =
    queryset = Habit.objects.all()
    # permission_classes = [IsModerator, IsOwner]


class LessonUpdateView(generics.UpdateAPIView):
    """ изменение привычки """
    # serializer_class =
    queryset = Habit.objects.all()
    # permission_classes = [IsModerator, IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    """ удаление привычки """
    queryset = Habit.objects.all()
    # permission_classes = [IsModerator, IsOwner]
