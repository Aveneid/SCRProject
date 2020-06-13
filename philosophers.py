import threading
import time


#Klasa Filozof, dziedziczy po klasie Thread
class Filozof(threading.Thread):

    #Konstruktor, przyjmujący parametry takie jak
    #nazwa, id lewego i prawego sztucca
    #oraz flage konca
    def __init__(self, name, stickl, stickr, ending):
        threading.Thread.__init__(self)
        self.name = name
        self.stickl = stickl
        self.stickr = stickr
        self.ending = ending
    
    #Glowna metoda klasy 
    def run(self):
        while not self.ending.is_set():
            self.think()
            self.dine()
    
    #Metoda odpowiadajaca za "myslenie / oczekiwanie" filozofa
    def think(self):
        print(self.name+ ' czeka. ')

    #Metoda odpowiadajaca za "konsumcje" przez filozofa
    def dine(self):
        print(self.name+ ' jest glodny. ')
        
        #Zablokowanie sztuccow dla instancji
        self.stickl.acquire()
        self.stickr.acquire()
        
        print(self.name+ ' je. ')
        print(self.name+ ' skonczyl jesc. ')
        
        #Odblokowanie sztuccow
        self.stickl.release()
        self.stickr.release()


#Tworzenie litsy z dostepnymi sztuccami
sticks = [threading.Lock() for i in range(5)]
#Inicjalizacja flagi konca "uczty"
ending = threading.Event()

#Lista z instancjami klasy Filozof zainicjowana odpowiednimi danymi
filozofowie = [Filozof('Filozof %i' % i, sticks[i%5], sticks[(i+1)%5], ending) for i in range(5)]

#Uruchomienie watka dla danej instancji klasy Filozof
for f in filozofowie:
    f.start()

#Krotka przerwa przed nastepnymi instrukcjami
time.sleep(10)

print('\n[[Koniec imprezy]]\n')
#Ustawienie flagi konca "uczty" - wymuszenie ukonczenia dzialan przez instancje klasy1
ending.set()

print('\n[[Oczekiwanie az filozofowie skoncza swoje czynnosci]]\n')

print("#####################")
print(filozofowie)
for f in filozofowie:
    print(f.join())
    f.join()
print(filozofowie)
print("#####################")
print('\nDziekuje dobranoc.')


