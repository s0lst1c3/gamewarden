import config
import sys

from core.scheduler.database import Scheduler_DB
from core.scheduler.job import Job
from core.scheduler.job import allowed_actions, allowed_days, isTimeFormat

db = None

def delete_one():

    cls()

    print_jobs()

    print 'Please enter the rowid of the job you wish to delete.'
    rowid = raw_input('Enter rowid: ')
    
    db.delete(rowid)
    db.commit()

    print
    print 'Job deleted.'
    print

    raw_input('Press enter to continue...')

def delete_all():

    cls()

    db.delete()
    db.commit()

    print 'All jobs deleted.'
    print

    raw_input('Press enter to continue...')

def get_action():

    # get action from user ----------------------------------------------------
    invalid_input = False 
    while True:

        cls()

        for index,action in enumerate(allowed_actions):

            print index,action
        print

        if invalid_input:
            print 'Invalid input.'
            print

        print 'Please select an action from the list above, or select the option for "daily".'
        print

        try:

            choice = int(raw_input('Enter choice: '))

            action = allowed_actions[choice]
            
            return action

        except ValueError:
            pass
        except IndexError:
            pass

        invalid_input = True

def get_day():

    # get day from user -------------------------------------------------------
    invalid_input = False 
    while True:

        cls()

        for index,day in enumerate(allowed_days):

            print index,day
        print

        if invalid_input:
            print 'Invalid input.'
            print

        print 'Please select an day from the list above, or select the option for "daily".'
        print

        try:

            choice = int(raw_input('Enter choice: '))

            day = allowed_days[choice]

            return day

        except ValueError:
            pass
        except IndexError:
            pass

        invalid_input = True

def get_stime():

    # get time from user -------------------------------------------------------
    invalid_input = False 
    while True:

        cls()

        if invalid_input:
            print 'Invalid input.'
            print
        print

        print 'Please enter time in the format HH:mm.'
        print 'Time must be in 24 hour format.'
        print 'Value of time must be within 00:00 through 23:59.'
        print
        print 'Examples: 11:39, 23:48, 01:39'
        print
        
        choice = raw_input('Enter time: ')
        if isTimeFormat(choice):

            return choice

        invalid_input = True

def insert_job():

    action = get_action()

    day = get_day()

    stime = get_stime()

    job = Job(day=day, stime=stime, action=action)

    cls()

    db.insert(job)
    db.commit()

    print 'Inserted job:'
    print
    if action == 'start_ap':
        print '    Action:    start access point'
    else:
        print '    Action:    stop access point'
    if day == 'daily':
        print '    Frequency: daily'
    else:
        print '    Frequency: every', day
    print '    Time:     ', stime
    print

    raw_input('Press enter to continue...')

def cls():

    print '\n' * 40

def print_jobs():

    for job in db.select():

        print job
    print

def print_jobs_menu():

    cls()

    for job in db.select():

        print job
    print

    raw_input('Press enter to continue...')

def quit():

    print 'Goodbye!'

    db.close()
    sys.exit()

main_menu_choices = {
    
    'Delete one entry' : delete_one,
    'Delete all entries' : delete_all,
    'Add new entry' : insert_job,
    'Quit' : quit,
    'Show scheduled jobs' : print_jobs_menu,
}

def main_menu():

    invalid_input = False
    while True:

        cls()
        for index,choice in enumerate(main_menu_choices):
            print index,choice
        print
        
        if invalid_input:
            print 'Invalid input.'
            print

        print 'Please select an option from the list above.'
        print

        try:

            choice = int(raw_input('Enter choice (0 through %d): ' % (len(main_menu_choices)-1)))
            selection =  main_menu_choices.values()[choice]
            return selection

        except IndexError:
            pass
        except ValueError:
            pass

        invalid_input = True

def run():

    global db
    db = Scheduler_DB()

    while True:

        selection = main_menu()
        selection()
        
    raw_input('Press enter to continue...')
