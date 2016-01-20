import sys
import os
import shutil
import random

def llenaHome():
    log = open(os.path.expanduser("~") + '/log.txt', 'w+')
    chorradas = open("chorradas.txt", 'r')

    for path, dirs, files in os.walk('./prueba'):
        name = random.choice(chorradas.readlines())
        if not os.path.exists(path + '/' + name): #no creo que existan pero bueno jajaja
            open(path + '/' + name, 'a')
            log.write(path + name + '\n')

    log.close()
