import json
import os

CHEMIN_PROJET = os.path.join("donnees", "projet.json")

def lire_nombre(message):
    """Demande un nombre positif à l'utilisateur avec gestion des erreurs."""
    while True:
        try:
            valeur = float(input(message))
            if valeur < 0:
                print("Erreur : veuillez entrer un nombre positif.")
            else:
                return valeur
        except ValueError:
            print("Erreur : saisie invalide, veuillez entrer un nombre.")

def saisir_ou_charger_projet():
    """Permet de saisir un nouveau projet ou de le charger depuis donnees/projet.json."""
    choix = input("1 - Saisir un nouveau projet / 2 - Charger un projet : ")

    if choix == "1":
        nom = input("Nom du projet : ")
        hauteur = lire_nombre("Hauteur des poteaux en m : ")
        epaisseur = lire_nombre("Epaisseur des semelles en m : ")

        projet = {
            "nom": nom,
            "hauteur": hauteur,
            "epaisseur": epaisseur,
            "poteaux": {}
        }

        for type_poteau in ["Angle", "Rive", "Central"]:
            print(f"\n--- Poteau : {type_poteau} ---")
            g = lire_nombre("Charge permanente G en kN : ")
            q = lire_nombre("Charge d'exploitation Q en kN : ")
            nombre = int(lire_nombre("Nombre de poteaux : "))

            projet["poteaux"][type_poteau] = {
                "G": g,
                "Q": q,
                "nombre": nombre
            }

        os.makedirs("donnees", exist_ok=True)
        with open(CHEMIN_PROJET, "w", encoding="utf-8") as fichier:
            json.dump(projet, fichier, indent=4, ensure_ascii=False)

        print(f"Projet '{nom}' enregistre avec succes dans {CHEMIN_PROJET}.")
        return projet

    elif choix == "2":
        try:
            with open(CHEMIN_PROJET, "r", encoding="utf-8") as fichier:
                projet = json.load(fichier)
            print("Projet charge avec succes :", projet["nom"])
            return projet
        except FileNotFoundError:
            print("Aucun fichier projet.json trouve dans le dossier donnees/.")
            return {}
        except json.JSONDecodeError:
            print("Erreur : le fichier JSON est corrompu.")
            return {}
    else:
        print("Choix invalide.")
        return {}