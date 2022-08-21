# ----------------------------------------------------------------------------------------
# PROGRAMA: Traductor
# ----------------------------------------------------------------------------------------
# Descripción: <<breve descripción>>
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
    idioma = eliminarTildes(input('Seleccione el idioma al que desea traducir (Ingles/Portugues): '))

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

salir = 'no'
while (salir != 'si'):
    print('Bienvenido al Traductor de días de la semana Español/Inglés - Español/Portugues. \n')
    traducir()
    salir = validarFinalizarInput('Si desea Finalizar el programa escriba si, de lo contrario escriba no: ')

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------