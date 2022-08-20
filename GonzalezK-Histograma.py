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

# <<Escriba desde aqui el código del programa...>>
def conjuntoDeValores ():
    conjuntoValores = []
    for i in range(10):
        valor = input('Ingrese el valor ' + str(i + 1) +' del conjunto de datos: ')
        conjuntoValores.append(valor)
        if i >= 4:
            finalizar = input('Desea continuar ingresando valores? si/no: ')
            if (finalizar == 'no'):
                return conjuntoValores
    return conjuntoValores

def histograma (longitud):
    histograma = []
    for i in range(longitud):
        valor = input('Ingrese el valor ' + str(i + 1) +' del histograma: ')
        histograma.append(valor)
    return histograma

def obtenerMaximosLocales (conjuntoValores, histograma):
    maximosLocales = []
    for i in range(1, len(histograma) - 1):
        if histograma[i] > histograma[i-1]:
            maximosLocales.append(conjuntoValores[i])
    return maximosLocales


print('Ingrese los valores del conjunto de valores/señal, de manera ascendente (mínimo 5 valores y máximo 10).')

listaConjuntoValores = conjuntoDeValores()
print('Su conjunto de valores es: ', listaConjuntoValores)

print('Ingrese ahora la frecuencia para cada valor del conjunto de datos en el orden adecuado (Histograma). \n'
      'Dado que la longitud de la señal/conjunto de datos es ', len(listaConjuntoValores), ',solo puede ingresar',
      len(listaConjuntoValores), 'valores.')
listaHistograma = histograma(len(listaConjuntoValores))
print('Su histograma es: ', listaHistograma)

print('Losmáximos locales son: ', obtenerMaximosLocales(listaConjuntoValores, listaHistograma))











# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------