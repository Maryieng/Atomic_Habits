from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        """ Создание Пользователя """
        self.user = User.objects.create(
            email='kass.o@yandex.ru',
            tg_name='@Maryieng',
            telegram_chat_id=610791877,
            password='12345'
        )

    def test_user_create(self):
        """ Создание Пользователя """
        data = {"email": "test@yandex.ru", "tg_name": "@test", "telegram_chat_id": 12345, "password": "test12345"}
        response = self.client.post(reverse('users:users_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_detail(self):
        """ Вывод информации о пользователе"""
        response = self.client.get(reverse('users:users_detail', kwargs={'pk': self.user.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_delete(self):
        """ Удаление Пользователя """
        response = self.client.delete(reverse('users:users_delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(id=self.user.pk).count(), 0)

    def test_user_update(self):
        """ Обновление информации по Пользователю """
        update_url = reverse('users:users_update', kwargs={'pk': self.user.pk})
        update_data = {'tg_name': 'string'}
        response = self.client.patch(update_url, update_data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.tg_name, update_data['tg_name'])
