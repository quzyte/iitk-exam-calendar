# global constants

avl_exams = ['Midsem', 'Endsem']
exam_type = ''		  # choose from one of the above
if not exam_type:
	exam_type=input('Enter exam type (one of \'Midsem\' or \'Endsem\'): ')
	for exam in avl_exams:
		if exam_type.lower() == exam.lower():
			exam_type = exam
	if exam_type not in avl_exams:
		print('Bad Input. Exiting...')
		exit()

roll = ''                   # your roll number, as a string
if not roll:
	roll=input('Enter roll number: ')

# enter email id if you wish to send yourself an email
# otherwise, leave it blank
email = ''
if not email:
	email=input('Enter your GMAIL ID if you wish to send yourself an email. (recommended way)\nGive a blank input if you choose not to: ')

reminders = [                     # add as many reminders as you wish by extending the list
    {                             # example reminder
        'weeks':   0, 
        'days':    0,
        'hours':   0,
        'minutes': 30,
        'seconds': 0		  # each field must be a non-negative integer

    },
    {                             # reminder 2
        'weeks':   1, 
        'days':    0,
        'hours':   0,
        'minutes': 0,
        'seconds': 0		  # each field must be a non-negative integer

    }
]

### do not edit beyond this

fileAddrs = {
    'Midsem':'http://172.26.142.68/examscheduler/',
    'Endsem':'http://172.26.142.68/examscheduler2/'
}

fileAddr = fileAddrs[exam_type]
file = 'personal_schedule.php'
query = '?rollno='
sem_file = 'top_bar.html'

# websites:
# http://172.26.142.68/examscheduler(2)/top_bar.html   for sem number
# http://172.26.142.68/examscheduler(2)/personal_schedule.php?rollno=   for schedule

