import datetime
from .models import Holidays, Outpass, Attendance

def count_days(start, end):
    ''' Checks the dates that exists between the from_date and return_date and also checks the number of days that lies in between
    '''
    d = start
    delta = datetime.timedelta(hours = 24)
    counter = 0
    while d <= end:
        print d.strftime("%Y-%m-%d")
        d += delta
        counter += 1
    return counter

min_out_time = datetime.time(15,00,00)
max_in_time  = datetime.time(10,00,00)
holiday = Holidays.objects.all()
list_holidays = []
for day in holiday :
    list_holiday.append(day.date.strftime("%Y-%m-%d"))

def check_date(start_date, start_time, end_date, end_time):
    ''' this function returns whether the permission is required or not.
    if the out_time is less than 3:00 pm. The time 3:00 pm is set by me, can be changed on request or suggestion by college administration.

    This method checks whether the leave period lies in holidays, if not then set permission_required = True. then message should be sent to the concerned faculty and staff.'''

    if start_time > min_out_time:    
        if end_date != start_date:
            d = start_date + datetime.timedelta(1)
    if end_time < max_in_time:
        if start_date != end_date :
            end_date = end_date + datetime.timedelta(-1)
    delta = datetime.timedelta(days = 1)
    dates = []
    while d <= end_date:
        dates.append(d.strftime("%Y-%m-%d"))
        d +=delta
    
    for day in dates:
        if day not in list_holiday:
            return True


##the true returned by this will be used to update whether the permission is required or not

