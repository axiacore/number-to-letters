#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from numbertoletters import number_to_letters


class TestToWord(unittest.TestCase):

    def test_to_word(self):
        numbers = [
            1,
            100,
            110,
            101,
            2000,
            102000,
            300000,
            4000000,
            500000000,
            999999998,
            826.02,
            203.01,
            21.1,
            0.24,
            0.00,
            -230.5,
            '2959163',
            '1000000',
            '150000',
        ]

        results = [
            'un',
            'cien',
            'ciento diez',
            'ciento un',
            'dos mil',
            'ciento dos mil',
            'trescientos mil',
            'cuatro millones',
            'quinientos millones',
            'novecientos noventa y nueve millones novecientos noventa y nueve '
            'mil novecientos noventa y ocho',
            'ochocientos veintiséis con dos',
            'doscientos tres con un',
            'veinti uno con diez',
            'cero con veinticuatro',
            'cero',
            'menos doscientos treinta con cincuenta',
            'dos millones novecientos cincuenta y nueve mil ciento sesenta y '
            'tres',
            'un millón',
            'ciento cincuenta mil',
        ]

        for result, number in zip(results, numbers):
            self.assertEqual(number_to_letters(number), result)
