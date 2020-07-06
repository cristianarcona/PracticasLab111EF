import os

EstNombres = ['Arun', 'Daniel', 'Cristian', 'Gabriel']
EstApellidos = ['Limachi', 'Rivera', 'Castro', 'Arcona']
EstCI = ['8463443', '6156166', '12764155', '9203136']
EstFechaNacimiento = [1994, 2004, 1994, 1990]
EstTelefono = ['71201944', '72002015', '69958966', '63227049']


def muestraMenu():
    print('')
    print('-------------------------------------- 0 --------------------------------------')
    print('Seleccione una opción ')
    print('')
    print('     1. Mostrar la lista de estudiantes')
    print('     2. Adicionar un estudiante')
    print('     3. Modificar un estudiante')
    print('     4. Eliminar un estudiante')
    print('     5. Consulta Salida cuarentena')
    print('     6. Consulta Votación Elecciones 2020')
    print('     0. Salir')
    print('')

def finPrograma():
    print('-------------------------------------- 0 --------------------------------------')
    print ('')
    print('0. Salir')
    print('1. Volver al menú principal')
    
def muestraEstudiantes():
    print('')
    print("Nombre:               ",EstNombres)
    print('')
    print("Apellido:             ",EstApellidos)
    print('')
    print("Carnet de indentidad: ",EstCI)
    print('')
    print("Fecha de nacimiento:  ",EstFechaNacimiento)
    print('')
    print("Telefono              ",EstTelefono)
    print('')

def adicionaEstudiante():
    # nombres
    print('')
    nuevoNombre = input('Ingrese el nombre: ')
    EstNombres.append(nuevoNombre)
    # apellidos
    print('')
    EstApellidos.append(input('Ingrese los apellidos: '))
    # CI
    print('')
    EstCI.append(input('Ingrese el CI: '))
    # Fecha de nacimiento
    print('')
    EstFechaNacimiento.append(input('Ingrese la fecha de nacimiento: '))
    # Telefono
    print('')
    EstTelefono.append(input('Ingrese el telefono: '))
    print('')
    print('Se han guardado los datos exitosamente')

def eliminaEstudiante():
    # ciBorrar = input('Ingrese el Carnet de Identidad del estudiante a borrar: ')
    # posicion = estudiantesCI.index(ciBorrar)
    posicion = EstCI.index(input('Ingrese el Carnet de Identidad del estudiante a borrar: '))
    EstNombres.pop(posicion)
    EstApellidos.pop(posicion)
    EstCI.pop(posicion)
    EstFechaNacimiento.pop(posicion)
    EstTelefono.pop(posicion)
    print('Se ha eliminado al estudiante.')

def modificaEstudiante():
    posicion = EstCI.index(input('Ingrese el Carnet de Identidad del estudiante a modificar: '))
    print(EstNombres[posicion])
    print(EstApellidos[posicion])
    print(EstCI[posicion])
    print(EstFechaNacimiento[posicion])
    print(EstTelefono[posicion])
    #ADICIONA LOS DATOS
    nuevoNombre = input('Ingrese el nombre: ')
    EstNombres.insert(posicion,nuevoNombre)
    # apellidos
    nuevoApellido = input('Ingrese los apellidos: ')
    EstApellidos.insert(posicion,nuevoApellido)
    # CI
    nuevoCI = input('Ingrese el CI: ')
    EstCI.insert(posicion,nuevoCI)
    # Fecha de nacimiento
    nuevoFechaNac = input('Ingrese la fecha de nacimiento: ')
    EstFechaNacimiento.insert(posicion,nuevoFechaNac)
    # Telefono
    nuevoTel = input('Ingrese el telefono: ')
    EstTelefono.insert(posicion,nuevoTel)
    #ELIMINA DATOS ANTERIORES
    a=posicion+1
    EstNombres.pop(a)
    EstApellidos.pop(a)
    EstCI.pop(a)
    EstFechaNacimiento.pop(a)
    EstTelefono.pop(a)
    print('')
    print('Se realizó la modificación del estudiante exitosamente.')


# Ingresar un dia y mostrar a los estudiantes que pueden salir ese dia
def consultaSalidaCuarentena():
    # Lun Mie Vie   impares
    # Mar Jue Sab   pares
    dia = input('Ingrese el dia que se desea validar (lun mie vie mar jue sab): ').lower()
    comparador = -1
    # LUN lun Lun LuN
    if dia in ['lun', 'mie', 'vie']:
        comparador = 1
        print('Los estudiantes que pueden salir son: ')
    elif dia in ['mar', 'jue', 'sab']:
        comparador = 0
        print('Los estudiantes que pueden salir son: ')
    else:
        print('Dia no registrado')                
    for i in range(len(EstNombres)):
        if int(EstCI[i]) % 2 == comparador:
            print(EstNombres[i])
            print(EstApellidos[i])
            print(EstCI[i])
            print(EstFechaNacimiento[i])
            print(EstTelefono[i])

def muestraEleciones():
    posicion = EstCI.index(input('Ingrese el Carnet de Identidad del estudiante a consultar: '))
    print('')
    print(EstNombres[posicion])
    print(EstApellidos[posicion])
    print(EstCI[posicion])
    print(EstFechaNacimiento[posicion])
    print(EstTelefono[posicion])
    a=EstFechaNacimiento[posicion]
    print('')
    if a>2001:
        print ("El estudiante",EstNombres[posicion],EstApellidos[posicion],"no está habilitado para votar en las siguientes elecciones del 06 de septiembre del 2020")
    else:
        print ("El estudiante",EstNombres[posicion],EstApellidos[posicion],"está habilitado para votar en las siguientes elecciones del 06 de septiembre del 2020")

def cabeceraMenu():
    print('-------------------------------------- 0 --------------------------------------')
    print('')

while True:
    os.system('cls')
    muestraMenu()
    print('-------------------------------------- 0 --------------------------------------')
    opcion = input()
    if opcion == '1':
        os.system('cls')
        cabeceraMenu()
        print('Esta es la lista de estudiantes registrados')
        muestraEstudiantes()
    elif opcion == '2':
        os.system('cls')
        cabeceraMenu()
        print('Ingrese los datos del estudiante nuevo')
        adicionaEstudiante()
    elif opcion == '3':
        os.system('cls')
        cabeceraMenu()
        modificaEstudiante()
    elif opcion == '4':
        os.system('cls')
        cabeceraMenu()
        eliminaEstudiante()
    elif opcion == '5':
        os.system('cls')
        cabeceraMenu()
        consultaSalidaCuarentena()
    elif opcion == '6':
        os.system('cls')
        cabeceraMenu()
        muestraEleciones()
    elif opcion == '0':
        os.system('cls')
        print('Gracias por utilizar el Sistema')
        break
    else:
        os.system('cls')
        print('Dato erroneo, Fin del programa')
        break
    finPrograma()
    print('')
    opcion2 = input()
    if opcion2 == '1':
        os.system('cls')
        print('')
        muestraEstudiantes()
    elif opcion2 == '0':
        os.system('cls')
        print('')
        print('Gracias por utilizar el Sistema')
        break
    else:
        os.system('cls')
        print('')
        print('Dato erroneo, Fin del Programa')
        break

# TODO: PERSISTENCIA

# TAREA1:    Crear e implementar el metodo modificar de las listas de estudiantes
# TAREA2:    Inventar una consulta cualquiera (como consultaSalidaCuarentena) y 
#            ponerla como opcion 6 
# TAREA3:    Mejorar el diseño en general

# Esta tarea vale como 2 tareas (semana del 25 de junio y semana del 02 de julio)
# Subir el codigo a sus repositorios en github y enviarme el enlace por 
# correo: arunwlh@outlook.com o por telegram: 71201944
