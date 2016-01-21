import sys
import os
import shutil
import random

def llenaHome():
    chorradas = open(os.path.expanduser("~") + "/Puteador/chorradas.txt", 'r')
    log = open(os.path.expanduser("~") + '/log.txt', 'w+')
    for path, dirs, files in os.walk('./prueba'):
        for i in range(1,6):
            name = chorradas.readline()
            if name == '':
                chorradas.close()
                chorradas = open(os.path.expanduser("~") + "/Puteador/chorradas.txt", 'r')
            if not os.path.exists(path + '/' + name + '.txt'): #no creo que existan pero bueno jajaja
                open(path + '/' + name + '.txt', 'a')
                log.write(path + name + '\n')

    log.close()
    return
