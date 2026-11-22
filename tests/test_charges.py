import unittest
from charge import calculer_n_elu, calculer_n_els


class TestCharges(unittest.TestCase):

    def test_calcul_n_elu(self):
        resultat = calculer_n_elu(80, 40)
        attendu = 168
        self.assertAlmostEqual(resultat, attendu)

    def test_calcul_n_els(self):
        resultat = calculer_n_els(80, 40)
        attendu = 120
        self.assertAlmostEqual(resultat, attendu)


if __name__ == "__main__":
    unittest.main()