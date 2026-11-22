import json
import os


DOSSIER_DONNEES = "donnees"
FICHIER_PROJET = os.path.join(DOSSIER_DONNEES, "projet.json")


def lire_nombre(message):
    while True:
        try:
            valeur = float(input(message))

            if valeur <= 0:
                print("Veuillez entrer un nombre positif.")
            else:
                return valeur

        except ValueError:
            print("Erreur : entrez un nombre valide.")


def saisir_projet():
    print("\n--- NOUVEAU PROJET ---")

    nom_projet = input("Nom du projet : ")

    hauteur = lire_nombre("Hauteur des poteaux en metres : ")
    epaisseur = lire_nombre("Epaisseur des semelles en metres : ")

    poteaux = {}

    types_poteaux = ["Angle", "Rive", "Central"]

    for type_poteau in types_poteaux:

        print(f"\n--- Poteaux {type_poteau} ---")

        nombre = int(lire_nombre("Nombre de poteaux : "))

        G = lire_nombre("Charge permanente G (kN) : ")
        Q = lire_nombre("Charge d'exploitation Q (kN) : ")

        poteaux[type_poteau] = {
            "G": G,
            "Q": Q,
            "nombre": nombre
        }

    projet = {
        "nom": nom_projet,
        "hauteur": hauteur,
        "epaisseur": epaisseur,
        "poteaux": poteaux
    }

    return projet


def sauvegarder_projet(projet):
    os.makedirs(DOSSIER_DONNEES, exist_ok=True)

    with open(FICHIER_PROJET, "w", encoding="utf-8") as fichier:
        json.dump(projet, fichier, indent=4, ensure_ascii=False)

    print("Projet sauvegarde avec succes.")


def charger_projet():
    if not os.path.exists(FICHIER_PROJET):
        print("Aucun projet sauvegarde.")
        return None

    with open(FICHIER_PROJET, "r", encoding="utf-8") as fichier:
        projet = json.load(fichier)

    print("Projet charge avec succes.")
    return projet


def saisir_ou_charger_projet():
    print("\n1 - Nouveau projet")
    print("2 - Charger un projet existant")

    choix = input("Votre choix : ")

    if choix == "1":
        projet = saisir_projet()
        sauvegarder_projet(projet)
        return projet

    elif choix == "2":
        return charger_projet()

    else:
        print("Choix invalide.")
        return None