from datetime import datetime, timedelta
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
        send_dates = [today + timedelta(seconds=5)]  # предложение оплатить придет через 5с после стартового сообщения
        count_of_days -= 1
        today += BREAK_BETWEEN_MESSAGES
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


