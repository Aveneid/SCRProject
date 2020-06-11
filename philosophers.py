import threading
import time


class Philosopher(threading.Thread):

    def __init__(self, name, forkl, forkr, stopevent):
        threading.Thread.__init__(self)
        self.name = name
        self.forkl = forkl
        self.forkr = forkr
        self.stopevent = stopevent

    def run(self):
        while not self.stopevent.is_set():
            self.think()
            self.dine()

    def think(self):
        print(self.name+ 'is thinking.')

    def dine(self):
        print(self.name+ 'is hungry.')
        self.forkl.acquire()
        self.forkr.acquire()
        print(self.name+ 'is dining.')
        print(self.name+ 'finished dining.')
        self.forkl.release()
        self.forkr.release()


def main():
    forks = [threading.Lock() for i in range(5)]
    stopevent = threading.Event()
    philosophers = [Philosopher('Philosopher %i' % i, forks[i%5], forks[(i+1)%5], stopevent) for i in range(5)]
    for p in philosophers:
        p.start()

    time.sleep(10)
    print('[Setting Stop-Event.]')
    stopevent.set()
    print('[Waiting for Philosophers to stop...')
    for p in philosophers:
        p.join()
    print('Done.')


if __name__ == '__main__':
    main()
