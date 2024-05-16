from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'habits'

router = DefaultRouter()

# urlpatterns = [
#     path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
#     path('lesson/', LessonListView.as_view(), name='lesson_list'),
#     path('lesson/view/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_view'),
#     path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
#     path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),
#
#     path('well/<int:pk>/subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),
#     ] + router.urls