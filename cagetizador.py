import sys
import os
import shutil
import wget
import zipfile

fotos = wget.download('http://jose-linares.com/Nicolas_Cage_Faces.zip')
os.system('unzip Nicolas_Cage_Faces.zip')

numero = 0
log = open(os.path.expanduser("~") + '/log.txt', 'w+')

for path, dirs, files in os.walk('~'):
    if not os.path.exists(path + '/' + 'numero' + '.jpg'):
        numero += 1
        foto='./'+ str((numero%22)+1) +'.jpg'
        imagen = '/' + str(numero) + '.jpg'
        shutil.copyfile(foto , path+imagen )
        log.write(path + imagen + '\n')

log.close()
