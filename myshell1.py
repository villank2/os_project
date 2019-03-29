import os,sys
import threading, multiprocessing
from cmd import Cmd
from functions import *
class MyPrompt(Cmd):

    def __init__(self):
        super().__init__(completekey='tab', stdin=None, stdout=None)
        self.path = os.getcwd()
        self.line = None
        self.lock = threading.Lock()
        self.plock = multiprocessing.Lock()
        self.threads = []
        if len(sys.argv) > 1:
            try:
                filename = sys.argv[1]
                with open(filename) as f:
                    self.cmdqueue.extend([line for line in f.readlines()])
                    self.cmdqueue.append("quit")
            except FileNotFoundError:
                print("No such file \"{}\"\nExiting...".format(filename))
                raise SystemExit

    def do_dir(self,args):
        fullcontents = os.listdir(self.path)
        maxlen = len(max(fullcontents,key=len))
        if len(args)>1:
            extension = "."+args.strip()
            self.threads = [threading.Thread(target=show_dir,args=(filename,maxlen,)) for filename in fullcontents if extension in filename]
        else:
            self.threads = [threading.Thread(target=show_dir,args=(filename,maxlen,)) for filename in fullcontents]
        print("{:{}} {:>10} {:^20} {:^20}".format("File-Name",maxlen,"Size","Created","Last Modified"))
        self.createThread()

    def do_cd(self,args):
        if args == "":
            return
        try:
            os.chdir(args)
            self.path = os.getcwd()
        except FileNotFoundError:
            print("File \"{}\" does not exist:".format(args))
        except NotADirectoryError:
            print("\"{}\" is not a directory".format(args))
        finally:
            self.prompt = self.path+">"

    def do_environ(self,args):
        dic = os.environ
        for k in dic.keys():
            print(k+dic[k])

    def do_quit(self,args):
        response = input("Exit <Y/N>?\n")
        if response == "Y":
            print("System Exit")
            raise SystemExit
        return
    def do_pause(self,args):
        self.plock.acquire()
        pause(self.lock)
        self.plock.release()
    def precmd(self,line):
        self.line = line
        return line

    def postcmd(self,stop,line):
        return stop

    def do_test(self,args):
        print(len(args))

    def createThread(self):
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()
        self.threads.clear()



if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = prompt.path+">"
    prompt.cmdloop()
