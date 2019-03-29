from multiprocessing import Process, Lock
from myshell1 import MyPrompt
def main():

def start_cmd():
    prompt = MyPrompt()
    prompt.prompt = prompt.path+" "
    prompt.cmdloop()
if __name__ == '__main__':
    main()
