# ----------------------------------------------------------------------------------------
# PROGRAMA: Histograma
# ----------------------------------------------------------------------------------------
# Descripción: Este programa se encarga de identificar los máximos locales en un histograma
# ingresado por el usuario
# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [20.08.2022]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variables de entrada: (str) valorConjunto, (int) valorHistograma, (boolean) salir, (boolean) finalizar
# pre-condiciones: valorConjunto, cada valor ingresado es string
#                  valorHistograma, cada valor ingresado debe ser int
#                  finalizar = 'no' o finalizar = 'si'
#                  salir != 'si'

# Variables auxiliares: ([]) conjuntoValores, ([]) histograma, (boolean),([]) maximosLocales, seguirPreguntando
#
# Explicación: Si salir es 'si', el programa dejará de ejecutarse.
#              valorConjunto, representa cada uno de los valores de la lista del Conjunto de Valores o Señal
#              (estos valores son ingresados por el usuario).
#              valorHistograma, representa cada uno de los valores de la lista del Histograma (estos valores son
#              ingresados por el usuario).
#              conjuntoValores, histograma, son las variables auxiliares usadas para formar las listas del
#              conjunto de valores y el histograma a partir de los datos ingresados por el usuario.
#              maximosLocales, variable auxiliar para almacenar los máximos locales
#              finalizar, es una variable usada para saber si el usuario desea a ingresar o no más valores a la
#              lista del conjunto de valores.
#              seguirPreguntando, es una variable auxiliar para saber si el programa debe volver a preguntar si:
#              'desea añadir más valores a la lista' o 'si desea salir del programa'.

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# Salida: Mensaje (string) informando si los máximos locales.

# Si salir == 'si' , fin del programa.

# ----------------------------------------------------------------------------------------

def validarValorHistograma (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        valorHistograma = input(mensaje)
        if valorHistograma.isdigit():
            seguirPreguntando = False
        else:
            print('El valor debe ser un número entero. Intente nuevamente.')
    return valorHistograma

def validarFinalizarInput (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        finalizar = input(mensaje)
        seguirPreguntando = not (finalizar == 'si' or finalizar == 'no')
    return finalizar

def conjuntoDeValores ():
    conjuntoValores = []
    for i in range(10):
        valorConjunto = input('Ingrese el valor ' + str(i + 1) +' del conjunto de datos: ')
        conjuntoValores.append(valorConjunto)
        if i >= 4:
            finalizar = validarFinalizarInput('Desea continuar ingresando valores? si/no:')
            if finalizar == 'no':
                return conjuntoValores
    return conjuntoValores

def histograma (longitud):
    histograma = []
    for i in range(longitud):
        valorHistograma = validarValorHistograma('Ingrese el valor ' + str(i + 1) +' del histograma: ')
        histograma.append(valorHistograma)
    return histograma

def obtenerMaximosLocales (conjuntoValores, histograma):
    maximosLocales = []
    for i in range(1, len(histograma) - 1):
        if histograma[i] > histograma[i-1]:
            maximosLocales.append(conjuntoValores[i])
    return maximosLocales

def determinarMaximosLocalesEnHistograma ():
    print('Ingrese los valores del conjunto de valores/señal, de manera ascendente (mínimo 5 valores y máximo 10).')

    listaConjuntoValores = conjuntoDeValores()
    print('Su conjunto de valores es: ', listaConjuntoValores, '\n')

    print('Ingrese ahora la frecuencia para cada valor del conjunto de datos en el orden adecuado (Histograma). \n'
          'Dado que la longitud de la señal/conjunto de datos es ', len(listaConjuntoValores), ', solo puede ingresar',
          len(listaConjuntoValores), 'valores.')
    listaHistograma = histograma(len(listaConjuntoValores))
    print('Su histograma es: ', listaHistograma, '\n \n')

    print('Conjunto de valores: ', listaConjuntoValores)
    print('Histograma: ', listaHistograma)
    if len(obtenerMaximosLocales(listaConjuntoValores, listaHistograma)) == 1:
        print('El máximo local es: ', obtenerMaximosLocales(listaConjuntoValores, listaHistograma))
    elif len(obtenerMaximosLocales(listaConjuntoValores, listaHistograma)) > 1:
        print('Los máximos locales son: ', obtenerMaximosLocales(listaConjuntoValores, listaHistograma))
    else:
       print('No hay máximos locales')


salir = 'no'

while (salir != 'si'):
    print('\n')
    determinarMaximosLocalesEnHistograma()
    salir = validarFinalizarInput('Si desea Finalizar el programa escriba si, de lo contrario escriba no: ')








# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------