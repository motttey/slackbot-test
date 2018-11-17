# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from datetime import datetime
from datetime import date
from datetime import timedelta

from math import ceil
import calendar

duty_dic = { 0:'B4', 1:'M1', 2:'M2', 3:'Doctor'}
part_num = 4

def get_start_end_dates(year, week):
    d = date(year,1,1)
    if (d.weekday() <= 3):
        d = d - timedelta(d.weekday())
    else:
        d = d + timedelta(7-d.weekday())
    dlt = timedelta(days = (week-1)*7)
    first_day = str(d + dlt);
    end_day = str(d + dlt + timedelta(days=6));
    return '( from: ' + first_day + ' to: ' + end_day + ' )'

@respond_to('hello')
def mention_func(message):
    message.reply('ゴミ')

@respond_to('今週のゴミ')
def mention_func(message):
    today = datetime.now()
    today_calender = today.isocalendar()
    duty_index = (today_calender[1] - 1) % part_num
    message.send('今週のゴミ担当は ' + duty_dic[duty_index] + ' です')

@respond_to('今月のゴミ')
def mention_func(message):
    first_day = date.today().replace(day=1)

    today = datetime.today()
    today_calender = datetime.now().isocalendar()
    first_day_calender = first_day.isocalendar()

    day_of_month = calendar.monthrange(today.year, today.month)
    week_number = int((day_of_month[1]) / 7)

    for w in range(1, week_number + 1):
        current_week = w + first_day_calender[1]
        duty_index = (current_week - 1) % part_num
        message.send(str(w)+ ' 週目 ' + get_start_end_dates(today_calender[0], current_week)+ 'のゴミ担当は' +duty_dic[duty_index]+ 'です')
