from datetime import date, timedelta


def yesterday():
    day = date.today()
    day_before = day - timedelta(days=1)
    return day_before
