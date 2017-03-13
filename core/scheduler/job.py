import time

allowed_days = [ 
    'sun',
    'mon',
    'tue',
    'wed',
    'thu',
    'fri',
    'sat',
    'daily',
]

allowed_actions = [

    'start_ap',
    'stop_ap',
]

def isTimeFormat(input):

    try:
        time.strptime(input, '%H:%M')
        return True

    except ValueError:
        return False

class Job(object):

    def __init__(self, day=None, stime=None, action=None, rowid=-1):

        assert stime is not None
        assert day is not None
        assert action is not None

        assert day in allowed_days
        assert action in allowed_actions
        assert isTimeFormat(stime)

        self.day = day
        self.stime = stime
        self.action = action
        self.rowid = rowid

            

    def __print__(self):
        return self.__str__()

    def __str__(self):
        return '< Job | %d | %s | %s | %s >' % (self.rowid, self.day, self.stime, self.action)
