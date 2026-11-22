from element import saisir_ou_charger_projet
from charge import calculer_poteau, descente_charges
from predimensionnement import predimensionner
from devis import generer_devis, exporter_rapport


def menu():
    """Affiche le menu principal et gere la navigation."""

    projet = {}

    while True:

        print("\n===== PROJET 1 : PREDIMENSIONNEMENT =====")
        print("1 - Saisir ou charger le projet")
        print("2 - Calculer le poteau")
        print("3 - Descente de charges")
        print("4 - Predimensionner les poteaux et semelles")
        print("5 - Generer le devis")
        print("6 - Exporter un rapport")
        print("0 - Quitter")

        choix = input("\nVotre choix : ")

        if choix == "1":

            nouveau_projet = saisir_ou_charger_projet()

            if nouveau_projet:
                projet = nouveau_projet

        elif choix == "2":

            calculer_poteau(projet)

        elif choix == "3":

            descente_charges(projet)

        elif choix == "4":

            predimensionner(projet)

        elif choix == "5":

            generer_devis(projet)

        elif choix == "6":

            exporter_rapport(projet)

        elif choix == "0":

            print("Fin du programme.")
            break

        else:

            print("Choix invalide, veuillez entrer un chiffre entre 0 et 6.")


if __name__ == "__main__":
    menu()