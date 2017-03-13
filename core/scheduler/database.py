import sqlite3
import config

from core.scheduler.job import Job

class Scheduler_DB(object):

    def __init__(self, db_name=config.scheduler_db):

        self.conn = sqlite3.connect(config.scheduler_db)
        self.cursor = self.conn.cursor()

    def insert(self, job):

        self.cursor.execute('INSERT INTO %s VALUES (?,?,?)' % config.scheduler_table, (job.action, job.day, job.stime,))

    def delete(self, rowid=None):

        if rowid is not None:
            self.cursor.execute('DELETE FROM %s where rowid=?' % config.scheduler_table, (rowid,))
        else:
            self.cursor.execute('DELETE FROM %s;' % config.scheduler_table)

    def select(self):

        for row in self.cursor.execute('SELECT rowid,* FROM %s;' % config.scheduler_table):
            yield Job(rowid=row[0], action=row[1], day=row[2], stime=row[3])

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
