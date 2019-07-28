# iitk-exam-calendar
> Directly create ical files of exam events and add them to your Google Calendar with just your roll number.

## Setup  
### Dependencies
This code uses the following python libraries:
- [requests](https://pypi.org/project/requests)   to get exam data
- [bs4](https://pypi.org/project/bs4)             to process that data
- [icalendar](https://pypi.org/project/icalendar) to create ical calendar files
- [pytz](https://pypi.org/project/pytz)           to set timezone in calendar
- [yagmail](https://pypi.org/project/yagmail)  (optional, but recommended. Read note for more details)

### Miscellaneous
- Have to be connected to IITK intranet for examscheduler to work
If you want to send yourself an email
- You also need to be connected to the internet
- You need to [enable less secure app access](https://myaccount.google.com/lesssecureapps) for your Google Account

## Install and Run
Install any dependencies not available already (using, for ex., `pip install name_of_library`)
To install, clone the repo (`git clone https://github.com/zargles/iitk-exam-calendar.git`)  
From the directory where you cloned the repository, run
```
cd iitk-exam-calendar
python3 exam_calendar.py
```
and supply details when prompted.  
Alternatively, you can manually edit config.py to add your details if you don't want to be prompted for your details every time.

### Example run
```
> git clone https://github.com/zargles/iitk-exam-calendar.git
Cloning into 'iitk-exam-calendar'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
> 
> cd iitk-exam-calendar && python3 exam_calendar.py 
Enter exam type (one of 'Midsem' or 'Endsem'): midsem
Enter roll number: 170656
Enter your GMAIL ID if you wish to send yourself an email. (recommended way)
Give a blank input if you choose not to: shashankhchandarr13579
2019-07-28 00:00:00+05:30
['CS682A', [17, 2, 19], [18, 0, 20, 0]]
['ESC201A', [19, 2, 19], [8, 0, 10, 0]]
['MTH301A', [18, 2, 19], [13, 0, 15, 0]]
['PHY210A', [21, 2, 19], [8, 0, 10, 0]]
['PHY226B', [], []]
['PSO201A', [22, 2, 19], [8, 0, 10, 0]]
['TA201A', [23, 2, 19], [8, 0, 10, 0]]
IITK Midsem Exam Schedule for 170656 for Semester 2018-19-2
Calendar ready: 170656_2018-19-2.ics
IITK Midsem Exam Schedule for 170656 for Semester 2018-19-2
Password for <shashankhchandarr13579@gmail.com>: 
Save username and password in keyring? [y/n]: n
> ls
170656_2018-19-2.ics  exam_calendar.py     __pycache__
config.py             helper_functions.py
```
  
### Note about sending email
Currently, There is some problem with Google Calendar on some browsers and it doesn't add _all_ the events from the calendar.  
  
That is why it is recommended to send yourself an email which you can directly open in the Gmail app to preview & add to your calendar.  
The code doesn't store or send your password anywhere. It is in the interest of security that the library `yagmail` has been used.  
This is an extremely lightweight library which handles passwords safely.
