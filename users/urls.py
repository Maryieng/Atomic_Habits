from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserAPIListView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path('', UserAPIListView.as_view(), name='users_list'),
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='users_delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
