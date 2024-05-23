from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.views import (HabitCreateView, HabitListView, HabitRetrieveView, HabitUpdateView, HabitDestroyView,
                          GetPublicHabitListView)

app_name = 'habits'

router = DefaultRouter()

urlpatterns = [
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('', HabitListView.as_view(), name='habit_list'),
    path('public_list', GetPublicHabitListView.as_view(), name='public_habit_list'),
    path('view/<int:pk>/', HabitRetrieveView.as_view(), name='habit_view'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyView.as_view(), name='habit_delete')] + router.urls
