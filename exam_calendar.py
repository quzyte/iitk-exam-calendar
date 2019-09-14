# all imports

from icalendar import Calendar, Event, vDatetime, Alarm
from datetime import datetime, timedelta
import pytz

from config import *
from helper_functions import *



sem = get_sem()

# calendar basic properties

now = datetime.now()
now = convert_datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
cal = Calendar()
cal.add('dtstamp', now)
# cal['dtstamp'] = now
# cal.add('name', 'IITK '+exam_type+' Exam Schedule for Semester '+sem)
cal['name'] = 'IITK '+exam_type+' Exam Schedule for '+roll+' for Semester '+sem
cal['summary'] = 'IITK '+exam_type+' Exam Schedule for Semester '+sem
cal['description'] = exam_type+' Exam calendar for '+roll+' for Semester '+sem+' made using data scraped from examscheduler iitk. Python source code at github.com/zargles'
cal.add('prodid', '-//zargles//iitk-exam-calendar//EN')
cal.add('version', '2.0')

print(now)
print(cal['name'])


# main code to enter exam events

keys, got_courses = get_courses(roll)
for exam_no, x in enumerate(got_courses):
    print(x)
    y = process_course([i for i in x], keys)
    # print(y)
    exam_course = y[keys['COURSE']]
    exam_date = y[keys['DAY']]
    exam_time = y[keys['SLOT']]
    if not exam_date:   # in case exam is not scheduled
        continue
    
    # an event per exam
    exam_event = Event()
    exam_event['uid'] = roll+'_'+sem+'.'+str(exam_no)+'@'+'iitk-exam-calendar'
    exam_event.add('dtstart', convert_datetime(2000+exam_date[2], exam_date[1], exam_date[0], hour=exam_time[0], minute=exam_time[1], second=0))
    exam_event.add('dtend', convert_datetime(2000+exam_date[2], exam_date[1], exam_date[0], hour=exam_time[2], minute=exam_time[3], second=0))
    exam_event['summary'] = exam_course+' '+exam_type
    exam_event['description'] = exam_course+' '+exam_type+'\nAdded from iitk-exam-calendar'
    exam_event.add('dtstamp', now)
    # exam_event.add('location', 'location unspecified')
    exam_event.add('status', 'CONFIRMED')
    
    for rem in reminders:
        exam_rem = Alarm()
        exam_rem.add('trigger', timedelta(weeks=-rem['weeks'], days=-rem['days'], hours=-rem['hours'], minutes=-rem['minutes'], seconds=-rem['seconds']))
        exam_rem.add('action', 'DISPLAY')
        exam_rem['description'] = 'Exam event reminder'
        exam_event.add_component(exam_rem)
    
    cal.add_component(exam_event)



# write to file
cal_name = roll+'_'+exam_type.lower()+'_'+sem+'.ics'
f = open(cal_name, 'wb')
f.write(cal.to_ical())
f.close()

print('\nCalendar ready:', cal_name,'\n')



if email:
	try:
		import yagmail
		subject = cal['name']
		contents = [cal['description'], 'Would you like to add this to your Google Calendar?', cal_name]
		yag = yagmail.SMTP(email)
		yag.send(subject=subject, contents=contents)
	except ModuleNotFoundError:
		print('Sending email requires \'yagmail\', a light and safe method to send emails. Install yagmail and try again')
