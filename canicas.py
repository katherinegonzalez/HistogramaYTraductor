# ----------------------------------------------------------------------------------------
# PROGRAMA: <<nombre del programa>>
# ----------------------------------------------------------------------------------------
# Descripción: <<breve descripción>>
# ----------------------------------------------------------------------------------------
# Autor: Luis Carlos Díaz
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import datetime   # modulo de python para este ejemplo (se usara para mostrar la fecha)

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

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
        diametroCanica = validarDiametroCanica('Ingrese el valor del diametro de la canica número ' + str(i + 1) +': ')
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