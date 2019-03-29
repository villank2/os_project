from datetime import datetime
import threading
import os.path
import sys
import time

def show_dir(filename,maxlen):
    if os.path.isfile(filename):
        size = os.path.getsize(filename)
        last_mod = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')
        creation = datetime.fromtimestamp(os.path.getctime(filename)).strftime('%Y-%m-%d %H:%M:%S')
        print("{:{}} {:>10} {:<20} {:<20}".format(filename,maxlen,size,creation,last_mod))
    elif os.path.isdir(filename):
        size = os.path.getsize(filename)
        print("{:{}}<DIR>{:>6}".format(filename,maxlen,size))

def sort_it():
    pass
def pause(lock):
    lock.acquire()
    ui = input()
    while ui != "":
        ui = input()
    lock.release()
