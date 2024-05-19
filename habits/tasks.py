from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import TGBot


@shared_task
def task_send_message():
    date_now = datetime.today().weekday()
    time_now = datetime.now().time().strftime('%H:%M')
    habits = Habit.objects.filter(sign_good_habit=False)

    for habit in habits:
        if habit.time.strftime('%H:%M') == time_now and habit.periodicity and date_now:
            chat_id = habit.user.telegram_chat_id
            text_message = (f"Пора {habit.action} на {habit.place}. "
                            f"На это тебе понадобится примерно {habit.time_to_complete} секунд.")
            if habit.reward:
                text_message += f"\nА в виде вознаграждения можешь {habit.reward}."
            message = TGBot()
            message.send_habit(text=text_message, chat_id=chat_id)
