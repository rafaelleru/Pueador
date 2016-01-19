import os

os.system('clear')

print "Escoja una opcion:\n"
print "\t 1. Bomba fork.(Solo en Linux)\n"
print "\t 2. Cagetizador.\n"



print "\t 3. Cambiar alias.\n"
print "\t 4. Trolling.\n"
print "\t 5. Llenar home de basura.\n"
#print "\t 6. Quijotizador.\n"

opcion = input('Introduzca una opcion:')

if opcion == '1':
    print 'Ejecuta Bomba fork'
elif opcion == '2':
    print 'Ejecuta Cagetizador'
elif opcion == '3':
    print 'Ejecuta Cambiar alias'
elif opcion == '4':
    print 'Ejecuta Trolling'
elif opcion == '5':
    print 'Ejecuta llenar home de basura'
else:
    print 'Opcion no valida.'
