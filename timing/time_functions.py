from datetime import datetime, timedelta

start_date = datetime.now()


def get_next_weekday(start_date, weekday_count):
    days_ahead = 0
    while weekday_count > 0:
        start_date += timedelta(days=1)
        if start_date.weekday() < 5:  # Понедельник=0, Вторник=1, ..., Пятница=4
            weekday_count -= 1
            days_ahead += 1
    return start_date

