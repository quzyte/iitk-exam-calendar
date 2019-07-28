# some helper functions

# all necessary imports
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from config import *


def cal_display(cal):
    return cal.to_ical().decode('utf8').replace('\r\n', '\n')


def get_sem():
    '''
    Function to get the ongoing semester details.
    Input: None
    
    Output: The current semester in the form: 'academic_year/sem_no.'
    
    This code does a minimal check, but it's not exhaustive.
    '''
    response = requests.get(fileAddr+sem_file, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    sem_details = [x.lower() for x in soup.p.text.split()]
    # print(sem_details)
    
    if 'first' in sem_details:
        semester = sem_details[2]+'-'+'1';
    elif 'second' in sem_details:
        semester = sem_details[2]+'-'+'2';
    else:
        raise FileNotFoundError('Semester neither First nor Second', sem_details);
    semester = semester.strip() # remove leading, trailing whitespace
    
    return semester;


def get_courses(roll):
    '''
    Function to get all courses of a student in the current semester
    Input: The roll number of the student you wish to get the results for.
    
    Output: Details of courses' exams that roll is doing this semester
    
    Note: This code doesn't check if the roll number is valid. It just returns what it can find
    '''
    
    response = requests.get(fileAddr+file+query+str(roll), timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', attrs={'class':'contenttable_lmenu'})
    # here, the attrs in not required really, because there is only one table in the page.
    # But following good practice, I have used an attribute found in the HTML file.
    details = []
    try:
        for row in table.findAll('tr'):
            course = [val.text.upper() for val in row.findAll('td')]
            details.append(course)
        keys = {key.upper():i for i, key in enumerate(details.pop(0))}
    except AttributeError as err:
        print(err.args, 'for roll', roll)
        keys, details = {}, []
    
    return (keys, details)


def process_course(course, keys):
    '''
    Function to process the courses returned by get_courses 
    and extract relevant details to make a calendar event
    '''
    # print(course[0])
    # course[0] stores the course ID,
    # course[1] stores the date,
    # and course[2] stores the start, end times
    for key in ['DAY', 'SLOT']:
        ind = keys[key]
        course[ind] = re.split('[^0-9]', course[ind]) # get readable data
        course[ind] = list(filter(None, course[ind]))  # remove empty strings
        course[ind] = [int(x) for x in course[ind]]
        # print(course[ind])
    return course


def convert_datetime(year, month, day, hour=0, minute=0, second=0):
    
    return pytz.timezone('Asia/Kolkata').localize(datetime(year, month, day, hour, minute, second))

