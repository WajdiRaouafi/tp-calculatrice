import unittest
import sys
import os
sys.path.append(os.path.abspath("."))

from src.calculatrice import division, puissance, moyenne
class TestCalculatrice(unittest.TestCase):

    def test_division_entiers(self):
        self.assertEqual(division(10, 2), 5.0)

    def test_division_decimales(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_resultat_float(self):
        self.assertIsInstance(division(9, 3), float)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    def test_puissance_classique(self):
        self.assertEqual(puissance(2, 3), 8.0)

    def test_puissance_exposant_zero(self):
        self.assertEqual(puissance(7, 0), 1.0)

    def test_puissance_type_float(self):
        self.assertIsInstance(puissance(2, 4), float)

    def test_puissance_exposant_negatif(self):
        with self.assertRaises(ValueError):
            puissance(2, -1)

    def test_moyenne_plusieurs_valeurs(self):
        self.assertEqual(moyenne([10, 20, 30]), 20.0)

    def test_moyenne_decimales(self):
        self.assertAlmostEqual(moyenne([1.5, 2.5]), 2.0)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])
