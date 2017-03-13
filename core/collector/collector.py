import os
import json
import random
import time
import sqlite3
import config

from core.collector import sniffer
from multiprocessing import Queue, Process
from datetime import datetime, timedelta


conn = None
cursor = None
counter = 0

def log_metadata():

        while True:

            probe_requests = sniffer.sniff_probes(config.collector_iface)

            for probe in probe_requests:

                # for testing purposes
                if probe is None:
                    continue
                    

                tx = probe['tx']
                src = probe['src']
                timestamp = probe['timestamp']

                store_result(tx, src, timestamp)

def store_result(tx, src, timestamp):

    global counter

    counter += 1
    cursor.execute('INSERT INTO visits VALUES (?,?,?)', (tx, src, timestamp,))

    if counter == 1:
        conn.commit()
        counter = 0


def run():

    global conn
    global cursor

    conn = sqlite3.connect(config.collector_db)
    cursor = conn.cursor()

    log_metadata()
    conn.close()

if __name__ == '__main__':
    run()
