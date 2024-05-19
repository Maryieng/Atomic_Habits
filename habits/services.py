import os
import requests


class TGBot:
    token = os.getenv('TELEGRAM_TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    def send_habit(self, text, chat_id):
        """ данные для отправки сообщений пользователю в телеграмме"""
        requests.post(
            url=f'{self.url}{self.token}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
