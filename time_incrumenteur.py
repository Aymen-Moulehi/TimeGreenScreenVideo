import datetime


def increment_time(time: datetime.time):
    second = time.second
    minute = time.minute
    hour = time.hour
    if second == 59:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
    else:
        second += 1
    return datetime.time(hour, minute, second)
