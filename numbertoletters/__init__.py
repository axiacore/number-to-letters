#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
UNIDADES = (
    '',
    'un ',
    'dos ',
    'tres ',
    'cuatro ',
    'cinco ',
    'seis ',
    'siete ',
    'ocho ',
    'nueve ',
    'diez ',
    'once ',
    'doce ',
    'trece ',
    'catorce ',
    'quince ',
    'dieciséis ',
    'diecisiete ',
    'dieciocho ',
    'diecinueve ',
    'veinte ',
)

UNIDADES_TILDES = {
    'un ': 'ún ',
    'dos ': 'dós ',
    'tres ': 'trés ',
    'seis ': 'séis ',
}

DECENAS = (
    'veinti',
    'treinta ',
    'cuarenta ',
    'cincuenta ',
    'sesenta ',
    'setenta ',
    'ochenta ',
    'noventa ',
    'cien ',
)
CENTENAS = (
    'ciento ',
    'doscientos ',
    'trescientos ',
    'cuatrocientos ',
    'quinientos ',
    'seiscientos ',
    'setecientos ',
    'ochocientos ',
    'novecientos ',
)


def number_to_letters(number):
    """Converts a number into string representation
    """
    converted = ''

    if isinstance(number, str):
        try:
            number = float(number)
        except ValueError:
            raise Exception('El valor ingresado es invalido')
    number, decimals = ('%.2f' % number).split('.')

    number = int(number)
    decimals = int(decimals)
    negative = number < 0
    if negative:
        number = abs(number)
    if not (0 <= number < 999999999):
        return 'No es posible convertir el numero a letras'

    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]

    if millones:
        if millones == '001':
            converted += 'un millón '
        elif int(millones) > 0:
            converted += '{}millones '.format(__convert_number(millones))

    if miles:
        if miles == '001':
            converted += 'mil '
        elif int(miles) > 0:
            converted += '{}mil '.format(__convert_number(miles))

    if cientos:
        if cientos == '001':
            converted += 'un '
        elif int(cientos) > 0:
            converted += __convert_number(cientos)
    if not number:
        converted = 'cero '

    if decimals:
        if converted.endswith('un '):
            converted = converted.replace('un ', ' uno ')
        elif converted.endswith('ún '):
            converted = converted.replace('ún ', ' uno ')
        decimals = number_to_letters(decimals)
        converted += 'con {}'.format(decimals)
    if negative:
        converted = 'menos {}'.format(converted)
    return converted.strip()


def __convert_number(n):
    """Max length must be 3 digits
    """
    output = ''

    if n == '100':
        output = 'cien '
    elif n[0] != '0':
        output = CENTENAS[int(n[0]) - 1]

    k = int(n[1:])
    if k <= 20:
        output += UNIDADES[k]
    else:
        decenas = DECENAS[int(n[1]) - 2]
        unidades = UNIDADES[int(n[2])]

        if decenas == 'veinti' and unidades in UNIDADES_TILDES:
            unidades = UNIDADES_TILDES[unidades]

        if (k > 30) & (n[2] != '0'):
            output += '{}y {}'.format(decenas, unidades)
        else:
            output += '{}{}'.format(decenas, unidades)

    return output
