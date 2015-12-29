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
        ]

        results = [
            'un ',
            'cien ',
            'ciento diez ',
            'ciento un ',
            'dos mil ',
            'ciento dos mil ',
            'trescientos mil ',
            'cuatro millones ',
            'quinientos millones ',
            'novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y ocho ',
        ]

        for result, number in zip(results, numbers):
            self.assertEqual(number_to_letters(number), result)
