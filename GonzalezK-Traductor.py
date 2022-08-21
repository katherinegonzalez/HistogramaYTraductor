# ----------------------------------------------------------------------------------------
# PROGRAMA: Traductor
# ----------------------------------------------------------------------------------------
# Descripción: Este programa traduce los días de la semana de español a inglés o a portugués
# de acuerdo a la selección del usuario.
# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [20.08.2022]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variables de entrada: (str) dia, (int) idioma, (str) salir
# pre-condiciones: dia, idioma, salir son string
#                  día debe ser: lunes, martes, miércoles, jueves, viernes, sábado, domingo
#                  idioma debe ser: Inglés, Portugués
#                  día, idioma: NO hay pre-condiciones para tíldes, mayúsculas o minúsculas
#                  (el string puede ser como sea)
#                  salir != 'si'
#

# Variables auxiliares: (dict) trans, (str) resultadoTraduccion, (bool) seguirPreguntando
#
# Explicación: Si salir es 'si', el programa dejará de ejecutarse.
#              dia, día de la semana ingresado por el usuario
#              idioma, idioma ingresado por el usuario para hacer la traducción
#              trans, variable auxiliar para quitarle las tíldes a una cadena
#              resultadoTraduccion, variable auxiliar para definir el mensaje final a mostrar en pantalla
#              seguirPreguntando, es una variable auxiliar para saber si el programa debe volver a preguntar
#              si desea salir del programa.

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# Salida: Mensaje (str) con la traducción del día dependiendo del idioma seleccionado.
#
# Si el día no es válido: Mensaje (str) informando ésto al usuario
# Si el idioma no es válido: Mensaje (str) informando ésto al usuario
# Si salir == 'si' , fin del programa.

# ----------------------------------------------------------------------------------------
# PARÁMETROS
# ----------------------------------------------------------------------------------------
# (dict) diasIngles, (dict) diasPortugues
# Estos son diccionarios que almacenan las traducciones de los días de la semana en inglés y portugués.

# (str) a,b
# Son parámetros auxiliares para quitar las tíldes a las cadenas introducidas
# ----------------------------------------------------------------------------------------

diasIngles = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'
}

diasPortugues= {
    'lunes': 'Segunda-feira',
    'martes': 'Terça-feira',
    'miercoles': 'Quarta-feira',
    'jueves': 'Quinta-feira',
    'viernes': 'Sexta-feira',
    'sabado': 'Sábado',
    'domingo': 'Domingo'
}

a, b = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
trans = str.maketrans(a, b)

def eliminarTildes (dia):
    return dia.translate(trans)

def traduccion (idioma, dia, mensajeDiaInvalido, mensajeIdiomaInvalido):
    if idioma == 'ingles':
        return diasIngles.get(dia, mensajeDiaInvalido)
    elif idioma == 'portugues':
        return diasPortugues.get(dia, mensajeDiaInvalido)
    else:
        return mensajeIdiomaInvalido

def traducir ():
    mensajeDiaInvalido = 'No es un día válido'
    mensajeIdiomaInvalido = 'No se encuentran resultados con el idioma introducido'

    dia = eliminarTildes(input('Ingrese el día de la semana que desea traducir: '))
    idioma = eliminarTildes(input('Seleccione el idioma al que desea traducir (Inglés/Portugués): '))

    resultadoTraduccion = traduccion(idioma.lower(), dia.lower(), mensajeDiaInvalido, mensajeIdiomaInvalido)

    if not resultadoTraduccion == mensajeDiaInvalido and not resultadoTraduccion == mensajeIdiomaInvalido:
        resultadoTraduccion = 'Traducción: ' + resultadoTraduccion

    print(resultadoTraduccion)

def validarFinalizarInput (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        finalizar = input(mensaje)
        seguirPreguntando = not (finalizar == 'si' or finalizar == 'no')
    return finalizar

print('Bienvenido al Traductor de días de la semana Español/Inglés - Español/Portugues.')
salir = 'no'
while (salir != 'si'):
    print('\n')
    traducir()
    salir = validarFinalizarInput('Si desea Finalizar el programa escriba si, de lo contrario escriba no: ')

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------