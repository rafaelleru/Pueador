import sys
import os
import shutil
import random

chorradas

def llenaHome():
    log = open(os.path.expanduser("~") + '/log.txt', 'w+')
    openChorradas()

    for path, dirs, files in os.walk('./prueba'):
        for i in range(1,6):
            name = random.choice(chorradas.readlines())
            if name == '':
                chorradas.close()
                openChorradas()
            if not os.path.exists(path + '/' + name): #no creo que existan pero bueno jajaja
                open(path + '/' + name, 'a')
                log.write(path + name + '\n')

    log.close()

def openChorradas():
    chorradas = open("chorradas.txt", 'r')
