import schedule
import time
import os
import config

from core.scheduler.database import Scheduler_DB

db = None

def run():

    db = Scheduler_DB()

    for job in db.select():
        add_to_schedule(job)

    while True:
        print 'test'
        schedule.run_pending()
        time.sleep(1)

def add_to_schedule(job):

    day = job.day
    stime = job.stime
    if job.action == 'start_ap':
        action = ap_start
    else:
        action = ap_stop

    if day == 'sun':
        schedule.every().sunday.at(stime).do(action)
    elif day == 'mon':
        schedule.every().monday.at(stime).do(action)
    elif day == 'tue':
        schedule.every().tuesday.at(stime).do(action)
    elif day == 'wed':
        schedule.every().wednesday.at(stime).do(action)
    elif day == 'thu':
        schedule.every().thursday.at(stime).do(action)
    elif day == 'fri':
        schedule.every().friday.at(stime).do(action)
    elif day == 'sat':
        schedule.every().saturday.at(stime).do(action)
    else: # daily
        schedule.every().day.at(stime).do(action)
    
def ap_start():

    print 'Starting AP'

    os.system('%s %s %s %s' %\
        (config.ap_start, config.iface,
            config.hostapd_conf, config.dnsmasq_conf))

def ap_stop():

    print 'Stopping AP'

    os.system('%s %s %s %s' %\
        (config.ap_stop, config.iface,
            config.hostapd_conf, config.dnsmasq_conf))

def test():
    print 'im working'
    
