import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from charge import calculer_n_elu


def test_calculer_n_elu():
    resultat = calculer_n_elu(100, 50)

    assert resultat == 210


def test_calculer_n_elu_zero():
    resultat = calculer_n_elu(0, 0)

    assert resultat == 0


def test_calculer_n_elu_sans_charge_exploitation():
    resultat = calculer_n_elu(100, 0)

    assert resultat == 135