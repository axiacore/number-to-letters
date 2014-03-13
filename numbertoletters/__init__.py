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
    'dieciseis ',
    'diecisiete ',
    'dieciocho ',
    'diecinueve ',
    'veinte ',
)
DECENAS = (
    'venti',
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

    number = int(number)    # TODO: support decimals
    if not (0 < number < 999999999):
        return 'No es posible convertir el numero a letras'

    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]

    if(millones):
        if(millones == '001'):
            converted += 'un millon '
        elif(int(millones) > 0):
            converted += '%smillones ' % __convertNumber(millones)

    if(miles):
        if(miles == '001'):
            converted += 'mil '
        elif(int(miles) > 0):
            converted += '%smil ' % __convertNumber(miles)

    if(cientos):
        if(cientos == '001'):
            converted += 'un '
        elif(int(cientos) > 0):
            converted += '%s ' % __convertNumber(cientos)

    return converted


def __convertNumber(n):
    """Max length must be 3 digits
    """
    output = ''

    if(n == '100'):
        output = 'cien '
    elif(n[0] != '0'):
        output = CENTENAS[int(n[0])-1]

    k = int(n[1:])
    if(k <= 20):
        output += UNIDADES[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%sy %s' % (DECENAS[int(n[1])-2], UNIDADES[int(n[2])])
        else:
            output += '%s%s' % (DECENAS[int(n[1])-2], UNIDADES[int(n[2])])

    return output
