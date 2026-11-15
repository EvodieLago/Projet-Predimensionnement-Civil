import json
import math

projet = {}


# 1. MENU PRINCIPAL

def menu():

    while True:

        print("\n===== PROJET 1 : PREDIMENSIONNEMENT =====")
        print("1 - Saisir ou charger le projet")
        print("2 - Calculer le poteau")
        print("3 - Descente de charges")
        print("4 - Predimensionner les poteaux et semelles")
        print("5 - Generer le devis")
        print("6 - Exporter un rapport")
        print("0 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            saisir_charger_projet()

        elif choix == "2":
            calculer_poteau()

        elif choix == "3":
            descente_charges()

        elif choix == "4":
            predimensionner()

        elif choix == "5":
            generer_devis()

        elif choix == "6":
            exporter_rapport()

        elif choix == "0":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")


# 2. SAISIR OU CHARGER LE PROJET

def saisir_charger_projet():

    global projet

    choix = input("1 - Saisir un projet / 2 - Charger un projet : ")

    if choix == "1":

        nom = input("Nom du projet : ")

        hauteur = float(input("Hauteur des poteaux en m : "))

        epaisseur = float(input("Epaisseur des semelles en m : "))

        projet = {
            "nom": nom,
            "hauteur": hauteur,
            "epaisseur": epaisseur,
            "poteaux": {}
        }

        for type_poteau in ["Angle", "Rive", "Central"]:

            print("\nPoteau :", type_poteau)

            g = float(input("Charge G en kN : "))

            q = float(input("Charge Q en kN : "))

            nombre = int(input("Nombre de poteaux : "))

            projet["poteaux"][type_poteau] = {
                "G": g,
                "Q": q,
                "nombre": nombre
            }

        fichier = open("projet.json", "w", encoding="utf-8")

        json.dump(projet, fichier, indent=4)

        fichier.close()

        print("Projet enregistre.")

    elif choix == "2":

        try:

            fichier = open("projet.json", "r", encoding="utf-8")

            projet = json.load(fichier)

            fichier.close()

            print("Projet charge :", projet["nom"])

        except FileNotFoundError:

            print("Aucun projet trouve.")

    else:

        print("Choix invalide.")


# 3. CALCULER LE POTEAU

def calculer_poteau():

    if projet == {}:
        print("Veuillez d'abord saisir un projet.")
        return

    for type_poteau, donnees in projet["poteaux"].items():

        g = donnees["G"]
        q = donnees["Q"]

        n_elu = 1.35 * g + 1.50 * q

        section = n_elu / 10000

        donnees["N_ELU"] = n_elu
        donnees["section"] = section

        print("\nPoteau :", type_poteau)
        print("N_ELU :", round(n_elu, 2), "kN")
        print("Section :", round(section, 3), "m2")


# 4. DESCENTE DE CHARGES

def descente_charges():

    if projet == {}:
        print("Veuillez d'abord saisir un projet.")
        return

    total = 0

    for type_poteau, donnees in projet["poteaux"].items():

        n_elu = 1.35 * donnees["G"] + 1.50 * donnees["Q"]

        charge = n_elu * donnees["nombre"]

        total = total + charge

        print("\nPoteau :", type_poteau)

        print("Charge par poteau :", round(n_elu, 2), "kN")

        print("Charge totale :", round(charge, 2), "kN")

    print("\nCharge totale du projet :", round(total, 2), "kN")


# 5. PREDIMENSIONNER LES POTEAUX ET LES SEMELLES

def predimensionner():

    if projet == {}:
        print("Veuillez d'abord saisir un projet.")
        return

    for type_poteau, donnees in projet["poteaux"].items():

        n_elu = 1.35 * donnees["G"] + 1.50 * donnees["Q"]

        section = n_elu / 10000

        cote = math.sqrt(section)

        cote_cm = cote * 100

        cote_retenu = max(20, math.ceil(cote_cm / 5) * 5)

        charge_semelle = donnees["G"] + donnees["Q"]

        cote_semelle = math.sqrt(charge_semelle / 187.5)

        cote_semelle = math.ceil(cote_semelle / 0.05) * 0.05

        donnees["cote_poteau"] = cote_retenu

        donnees["cote_semelle"] = cote_semelle

        print("\nPoteau :", type_poteau)

        print("Cote du poteau :", cote_retenu, "cm")

        print("Cote de la semelle :", round(cote_semelle, 2), "m")


# 6. GENERER LE DEVIS

def generer_devis():

    if projet == {}:
        print("Veuillez d'abord saisir un projet.")
        return

    volume_total = 0

    for donnees in projet["poteaux"].values():

        if "cote_poteau" not in donnees:
            print("Effectuez d'abord le predimensionnement.")
            return

        cote = donnees["cote_poteau"] / 100

        semelle = donnees["cote_semelle"]

        nombre = donnees["nombre"]

        volume_poteau = cote * cote * projet["hauteur"] * nombre

        volume_semelle = semelle * semelle * projet["epaisseur"] * nombre

        volume_total = volume_total + volume_poteau + volume_semelle

    prix = float(input("Prix du beton par m3 en FCFA : "))

    montant = volume_total * prix

    print("\n--- DEVIS ---")

    print("Volume total :", round(volume_total, 3), "m3")

    print("Prix du beton :", prix, "FCFA")

    print("Montant total :", round(montant), "FCFA")

    projet["volume"] = volume_total
    projet["montant"] = montant


# 7. EXPORTER UN RAPPORT

def exporter_rapport():

    if projet == {}:
        print("Veuillez d'abord saisir un projet.")
        return

    fichier = open("rapport.txt", "w", encoding="utf-8")

    fichier.write("RAPPORT DU PROJET\n")

    fichier.write("Projet : " + projet["nom"] + "\n")

    for type_poteau, donnees in projet["poteaux"].items():

        n_elu = 1.35 * donnees["G"] + 1.50 * donnees["Q"]

        fichier.write("\nPoteau : " + type_poteau + "\n")

        fichier.write("N_ELU : " + str(round(n_elu, 2)) + " kN\n")

        if "cote_poteau" in donnees:

            fichier.write("Cote poteau : " + str(donnees["cote_poteau"]) + " cm\n")

            fichier.write("Cote semelle : " + str(donnees["cote_semelle"]) + " m\n")

    if "volume" in projet:

        fichier.write("\nVolume beton : " + str(round(projet["volume"], 3)) + " m3\n")

        fichier.write("Montant : " + str(round(projet["montant"])) + " FCFA\n")

    fichier.close()

    print("Rapport exporte dans rapport.txt")


# LANCEMENT DU PROGRAMME

menu()
