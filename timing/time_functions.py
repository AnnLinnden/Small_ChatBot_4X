from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import BREAK_BETWEEN_MESSAGES


class ScheduleMessages:
    def __init__(self):
        job_storage = {'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')}
        self.scheduler = AsyncIOScheduler(jobstores=job_storage)
        self.scheduler.start()

    def create_list_of_send_dates(self, count_of_days):
        today = datetime.today()
        send_dates = [today]
        count_of_days -= 1
        while count_of_days > 0:
            if today.weekday() < 5:  # Понедельник=0, Вторник=1, ..., Пятница=4
                send_dates.append(today)
                count_of_days -= 1
            today += BREAK_BETWEEN_MESSAGES
        return send_dates

    def schedule_messages(self, function, run_date, chat_id):
        self.scheduler.add_job(
            func=function,
            coalesce=True,
            trigger=DateTrigger(run_date=run_date),
            kwargs={'chat_id': chat_id}
        )

    def check(self):
        self.scheduler.print_jobs()

    # async def send_message(self, user_id, text):
    #     await bot.send_message(chat_id=user_id, text=text)
    #
    # def get_next_date(self, start_date, messages_count):
    #     while messages_count > 0:
    #         start_date += timedelta(days=1)
    #         if start_date.weekday() < 5:  # Понедельник=0, Вторник=1, ..., Пятница=4
    #             messages_count -= 1
    #     return start_date
    #
    # def schedule_messages(self, user_id, start_date):
    #     for i, message in enumerate(messages.message_chain):
    #         send_date = self.get_next_date(start_date, i)
    #         self.scheduler.add_job(
    #             self.send_message,
    #             trigger=DateTrigger(run_date=send_date),
    #             args=(user_id, message)
    #         )


