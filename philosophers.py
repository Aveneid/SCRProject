import threading
import time

class Filozof(threading.Thread):

    def __init__(self, name, stickl, stickr, ending):
        threading.Thread.__init__(self)
        self.name = name
        self.stickl = stickl
        self.stickr = stickr
        self.ending = ending

    def run(self):
        while not self.ending.is_set():
            self.think()
            self.dine()

    def think(self):
        print(self.name+ ' czeka. ')

    def dine(self):
        print(self.name+ ' jest glodny. ')
        self.stickl.acquire()
        self.stickr.acquire()
        print(self.name+ ' je. ')
        print(self.name+ ' skonczyl jesc. ')
        self.stickl.release()
        self.stickr.release()



sticks = [threading.Lock() for i in range(5)]
ending = threading.Event()
filozofowie = [Filozof('Filozof %i' % i, sticks[i%5], sticks[(i+1)%5], ending) for i in range(5)]

for f in filozofowie:
    f.start()
time.sleep(10)
print('\n[[Koniec imprezy]]\n')
ending.set()

print('\n[[Oczekiwanie az filozofowie skoncza swoje czynnosci]]\n')
for f in filozofowie:
    f.join()
print('\nDziekuje dobranoc.')


