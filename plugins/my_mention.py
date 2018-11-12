# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from datetime import datetime
from datetime import date
from math import ceil

duty_dic = { 0:'B4', 1:'M1', 2:'M2', 3:'Doctor'}
@respond_to('gomiday')
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ')

@respond_to('今週のゴミ')
def mention_func(message):
    today = datetime.now()
    today_calender = today.isocalendar()
    duty_index = today_calender[2] % 4
    message.reply('今週のゴミ担当は' + duty_dic[duty_index] + 'です')

@respond_to('今月のゴミ')
def mention_func(message):
    day_of_month = datetime.now().day
    week_number = (day_of_month - 1) % 7
    first_day = date.today().replace(day=1)

    today = datetime.now()
    today_calender = today.isocalendar()
    first_day_calender = today.isocalendar()

    for w in range(week_number):
        duty_index = (w + today_calender[2] - first_day_calender[2]) % 4
        message.reply(str(w)+ '週目のゴミ担当は' +duty_dic[duty_index]+ 'です')
