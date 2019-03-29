import os,threading,multiprocessing
import sys,time
from functions import *
from cmd import Cmd
class MyShell(Cmd):
    def __init__(self):
        super().__init__(completekey='tab', stdin=None, stdout=None)
        self.path = os.getcwd()
        self.line = None
        self.tlock = threading.Lock()
        self.plock = multiprocessing.Lock()
        self.threads = []
        if len(sys.argv) > 1:
            try:
                filename = sys.argv[1]
                with open(filename) as f:
                    self.cmdqueue.extend([line for line in f.readlines()])
                    #self.cmdqueue.append("quit")
            except FileNotFoundError:
                print("No such file \"{}\"\nExiting...".format(filename))
                raise SystemExit


    def do_dir(self,args):
        self.plock.acquire()
        print(os.listdir(self.path))
        self.plock.release()

    def do_pause(self,args):
        self.plock.acquire()
        enter = ""
        s = input()
        while not s is enter:
            s = input()
        self.plock.release()


if __name__ == '__main__':
    prompt = MyShell()
    prompt.prompt = prompt.path+">"
    prompt.cmdloop()
