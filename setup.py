import os
import sqlite3
import config

def initialize_dbs():

    os.system('rm %s' % config.scheduler_db)
    os.system('rm %s' % config.collector_db)

    conn = sqlite3.connect(config.scheduler_db)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE %s (action text, day text, stime text)' % config.scheduler_table)
    conn.commit()

    conn = sqlite3.connect(config.collector_db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE visits (tx integer, mac text, ts datetime, seq integer)''')
    conn.commit()

    conn.close()

if __name__ == '__main__':
    initialize_dbs()
