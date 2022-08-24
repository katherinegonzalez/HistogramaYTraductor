# ----------------------------------------------------------------------------------------
# PROGRAMA: Clasificador de canicas
# ----------------------------------------------------------------------------------------
# Descripción: Este programa se encarga clsificar N cantidad de canicas de acuerdo a los
# diámetros de cada una de ellas, los cuales son ingresados por el usuario

# ----------------------------------------------------------------------------------------
# Autores: Lorena Patricia Mora Hernandez - Katherine Xiomar González Santacruz
# Version: 1.0
# [23.08.2022]
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variables de entrada: (int) numeroCanicas, (int) diametroCanica, (str) salir
# pre-condiciones: numeroCanicas, debe ser un entero mayor o igual que 3 y menor o igual que 10
#                  diametroCanica, cada valor ingresado debe ser int
#                  salir != 'si'

# Variables auxiliares: (int) numeroMultiplos, (list) listaDiametros, (int) totalBuenas,
#                       (int) totalPotBuenas, (int) totalMalas, (bool) seguirPreguntando
#
# Explicación: Si salir es 'si', el programa dejará de ejecutarse.
#              numeroCanicas, representa el número de canicas que el usuario quiere clasificar.
#              diametroCanica, cada uno de los diámetros de las canicas ingresados por el usuario.
#              numeroMultiplos, variable auxiliar para contar cuantos múltiplos tiene un diametro.
#              listaDiametros, variable para almacenar la lista de todos los diámetros ingresados por el usuario.
#              totalBuenas, variable auxiliar para contar el número de canicas buenas,
#              totalPotBuenas, variable auxiliar para contar el número de canicas potencialmente buenas,
#              totalMalas, variable auxiliar para contar el número de canicas malas,
#              seguirPreguntando, es una variable auxiliar para saber si el programa debe volver a preguntar: sobre
#              ingresar un dato, o si desea salir del programa (dependiendo del caso en que se use)

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# Salida: Mensaje (str) informando la clasificación de cada una de las canicas y el numero de canicas buenoas,
# potencialmente buenas y malas.

# Si salir == 'si' , fin del programa.

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# buena, potBuena, mala, son parámetros para almacenar los tipos de clasificacion

# ----------------------------------------------------------------------------------------

buena = 'Buena'
potBuena = 'Potencialmente buena'
mala = 'Mala'

def validarFinalizarInput (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        finalizar = input(mensaje)
        seguirPreguntando = not (finalizar == 'si' or finalizar == 'no')
    return finalizar

def tipoClasificacion(numeroMultiplos):
    if (numeroMultiplos == 3):
        return buena
    elif (numeroMultiplos >= 1 and numeroMultiplos < 3):
        return potBuena
    else:
        return mala

def clasificadorCanica(diametro):
    numeroMultiplos = 0

    if (diametro % 2 == 0):
        numeroMultiplos += 1

    if (diametro % 3 == 0 ):
        numeroMultiplos += 1

    if (diametro % 5 == 0):
        numeroMultiplos += 1

    return tipoClasificacion(numeroMultiplos)

def getNumeroCanicas ():
    seguirPreguntando = True
    while seguirPreguntando:
        numeroCanicas = input('¿Cuántas canicas desea clasificar? (Mínimo permitido: 3, Máximo permitido: 10)')
        if numeroCanicas.isdigit() and int(numeroCanicas) >= 3 and int(numeroCanicas) <= 10:
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido.')
    return int(numeroCanicas)

def validarDiametroCanica (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        diametroCanica = input(mensaje)
        if diametroCanica.isdigit():
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido.')
    return int(diametroCanica)

def getDiametrosCanicas (numeroCanicas):
    listaDiametros = []
    for i in range(numeroCanicas):
        diametroCanica = validarDiametroCanica('Ingrese el valor del diámetro de la canica número ' + str(i + 1) +': ')
        listaDiametros.append(diametroCanica)
    return listaDiametros

def palabraPluralSingular(numero, tipo):
    if (numero > 1 or numero == 0):
        return tipo+'s'
    elif (numero == 1):
        return tipo

def clasificadorDeCanicas ():
    numeroCanicas = getNumeroCanicas()
    listaDiametros = getDiametrosCanicas(numeroCanicas)

    totalBuenas = 0
    totalPotBuenas = 0
    totalMalas = 0

    print('\n')
    print('Clasificación: ')
    for i in range(numeroCanicas):
        clasificacionCanica = clasificadorCanica(listaDiametros[i])

        print('Canica ', i+1, ': ', clasificacionCanica)

        if (clasificacionCanica == buena):
            totalBuenas += 1
        elif (clasificacionCanica == potBuena):
            totalPotBuenas += 1
        elif (clasificacionCanica == mala):
            totalMalas += 1

    print('\n')
    print('Total:')
    print(totalBuenas, palabraPluralSingular(totalBuenas, buena))
    print(totalPotBuenas, palabraPluralSingular(totalPotBuenas, potBuena), ' y')
    print(totalMalas, palabraPluralSingular(totalMalas, mala))



print('¡Clasificador de Canicas!')
salir = 'no'

while (salir != 'si'):
    print('\n')
    clasificadorDeCanicas()
    salir = validarFinalizarInput('Si desea Finalizar el programa escriba si, de lo contrario escriba no: ')



# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------