from concurrent.futures import process
from random import random
from linkedlist import LinkedList
from enum import Enum
from threading import Thread
from random import randint
import time
from os import system


class Status(Enum):
    DONE = 0
    READY = 1
    RUNNING = 2

class RoundRobin(Thread):
    def __init__(self, list: LinkedList, quantum):
        Thread.__init__(self)
        self.list = list
        self.quantum = quantum


    def run(self):
        doneCount=0
        while True:
            proc = self.list.getNextNode()
            if proc[2] == Status.READY:
                proc[2] = Status.RUNNING
                proc[1] -= self.quantum
                time.sleep(self.quantum/1000)
                if proc[1] <= 0:
                    proc[2] = Status.DONE
                    doneCount += 1 
                    proc[1] = 0
                else:
                    proc[2] = Status.READY
            if doneCount >= self.list.getCount():
                break


lista = LinkedList()

for id in range(5):
    lista.append([id, randint(34,132), Status.READY])

rb = RoundRobin(lista, 12)
rb.start()

for i in range(5,56,1):
    lista.append([i, randint(34,132), Status.READY])
    time.sleep(randint(11,76)/1000)
    system('cls')
    print(lista)


while rb.is_alive():
    system('cls')
    print(lista)
    time.sleep(0.05)

