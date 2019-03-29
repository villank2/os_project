import multiprocessing

def main():
    lock = multiprocessing.Lock()
    test2(lock)
    test1(lock)
    test2(lock)


def test1(lock):
    lock.acquire()
    print("test1 has lock")

def test2(lock):
    lock.acquire()
    print("test2 has lock\nreleasing now")
    lock.release()

if __name__ == '__main__':
    main()
