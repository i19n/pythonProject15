import datetime
import dateutil
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Fixdata:
    __day__=['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
    __mounth__=['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']

    def day(str):
        for i in Fixdata:
            if i in str:
                if str[str.find(i) - 3].isdigit():
                    return str[str.find(i) - 3:str.find(i) - 1]
                else:
                    return str[str.find(i) - 2:str.find(i) - 1]
        return None
    def mounth(str):
        for i in Fixdata:
            if i in str:
                return FixDataFinder.__months__.index(i) + 1
        return None
    def year(str):
        txt='года'
        if i in str:
            return str[str.find(i) - 5:str.find(i) - 1]
        else:
            return None
    def time(str):
        global MESSAGE
        if 'утром' in str or 'вечером' in str or 'днем' in str:
            if 'утром' in str:
                MESSAGE['DATE']['hour'] = 9
                MESSAGE['DATE']['minute'] = 0
            elif 'днем' in str:
                MESSAGE['DATE']['hour'] = 13
                MESSAGE['DATE']['minute'] = 0
            elif 'вечером' in str:
                MESSAGE['DATE']['hour'] = 19
                MESSAGE['DATE']['minute'] = 0
        elif str.rfind(':') and str[str.rfind(':') - 1].isdigit() and str[str.rfind(':') + 1].isdigit():
            time = str[str.rfind(':') - 2:str.rfind(':') + 3]
            if time[0] == ' ':
                MESSAGE['DATE']['hour'] = time[1:2]
                MESSAGE['DATE']['minute'] = time[3:]
            else:
                MESSAGE['DATE']['hour'] = time[:2]
                MESSAGE['DATE']['minute'] = time[3:]

    def dayofweek(str):
        for i in FixDataFinder.__week__:
            if i in str:
                if datetime.now().weekday() < FixDataFinder.__week__.index(i):
                    return FixDataFinder.__week__.index(i) - datetime.now().weekday()

def deletedata(str):
    __day__ = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    __mounth__=['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
    for i in __day__:
        if i in str:
            return str[:str.find(i)-3]
    for i in __months__:
        if i in str:
            return str[:str.find(i) - 3]
    if 'через' in str:
        return str[:str.find('через')-1]
    else:
        for i in str:
            if i.isdigit():
                str=str[:str.find(i)-1]
                if str[-1]=='в' and str[-2]==' ':
                    str=str[:-2]
                return str

def dynamictime(list):
    global current_time
    if len(list) == 1:
        if list[0] == 'год':
            current_time += timedelta(years=1)
        elif list[0] == 'час':
            current_time += timedelta(hours=1)
        elif list[0] == 'день':
            current_time += timedelta(days=1)
        elif list[0] == 'месяц':
            current_time += timedelta(months=1)
        elif list[0] == 'минуту':
            current_time += timedelta(minutes=1)
        elif list[0] == 'неделю':
            current_time += timedelta(days=7)
    elif list[1] == 'года' or list[1] == 'лет':
        current_time += timedelta(years=int(list[0]))
    elif list[1] == 'месяца' or list[1] == 'месяцев':
        current_time += timedelta(months=int(list[0]))
    elif list[1] == 'месяц':
        current_time += timedelta(months=1)
    elif list[1] == 'дня' or list[1] == 'дней':
        current_time += timedelta(days=int(list[0]))
    elif list[1] == 'день':
        current_time += timedelta(days=1)
    elif list[1] == 'часа' or list[1] == 'часов':
        current_time += timedelta(hours=int(list[0]))
    elif list[1] == 'час':
        current_time += timedelta(hours=1)
    elif list[1] == 'минут' or list[1] == 'минуты':
        current_time += timedelta(minutes=int(list[0]))
    elif list[1] == 'минуту':
        current_time += timedelta(minutes=1)
    elif list[1] == 'недель':
        current_time += timedelta(days=7 * list[0])

def update(n):
    MESSAGE['DATE']['year'] = n.year
    MESSAGE['DATE']['month'] = n.month
    MESSAGE['DATE']['day'] = n.day
    MESSAGE['DATE']['hour'] = n.hour
    MESSAGE['DATE']['minute'] = n.minute

def num(str):
        str=str[str.rfind('числа')-3:str.rfind('числа')-1]
        if str[0]=='':
            str=str[1:]
        n=datetime.now()
        if int(str)<int(datetime.now().day):
            n+=relativedelta(months=1)
            n-=relativedelta(days=c.day-int(str))
            return n
        else:
            n+=timedelta(days=int(str)-c.day)
            return n