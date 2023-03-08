import datetime

def fiveDaysAgo():
    fiveDays = datetime.date.today() - datetime.timedelta(days = 5)
    return fiveDays

def yesterdayTodayTomorrow():
    yesterday = datetime.date.today() - datetime.timedelta(days = 1)
    tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
    today = datetime.date.today()
    return f"Yesterday: {yesterday}\nToday: {today}\nTomorrow: {tomorrow}"

def droppingMicroSeconds():
    today = datetime.datetime.now()
    today = str(today)
    dateWithoutMseconds = today.split(".")
    return dateWithoutMseconds[0]
# print(droppingMicroSeconds())

def diff():
    dt1 = datetime.datetime.now()
    dt2 = datetime.datetime.now() - datetime.timedelta(days = 19)
    delta = dt1 - dt2
    return delta.total_seconds()
# print(diff())
