from element import lire_nombre
from charge import calculer_n_elu

def generer_devis(projet):
    """Calcule le volume total de béton et génère le devis en FCFA."""
    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    volume_total = 0
    for donnees in projet["poteaux"].values():
        if "cote_poteau" not in donnees:
            print("Erreur : effectuez d'abord le predimensionnement (Option 4).")
            return

        cote = donnees["cote_poteau"] / 100
        semelle = donnees["cote_semelle"]
        nombre = donnees["nombre"]

        volume_poteau = cote * cote * projet["hauteur"] * nombre
        volume_semelle = semelle * semelle * projet["epaisseur"] * nombre
        volume_total += volume_poteau + volume_semelle

    prix = lire_nombre("Prix du beton par m3 en FCFA : ")
    montant = volume_total * prix

    print("\n--- DEVIS ESTIMATIF ---")
    print(f"Volume total de beton : {round(volume_total, 3)} m3")
    print(f"Prix unitaire : {prix} FCFA")
    print(f"Montant total : {round(montant)} FCFA")

    projet["volume"] = volume_total
    projet["montant"] = montant

def exporter_rapport(projet):
    """Exporte l'ensemble des résultats dans un fichier rapport.txt."""
    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    with open("rapport.txt", "w", encoding="utf-8") as fichier:
        fichier.write("=========================================\n")
        fichier.write("   RAPPORT DE PREDIMENSIONNEMENT - IIT   \n")
        fichier.write("=========================================\n")
        fichier.write(f"Projet : {projet['nom']}\n")

        for type_poteau, donnees in projet["poteaux"].items():
            n_elu = calculer_n_elu(donnees["G"], donnees["Q"])
            fichier.write(f"\n--- Poteau : {type_poteau} ---\n")
            fichier.write(f"Nombre : {donnees['nombre']}\n")
            fichier.write(f"N_ELU : {round(n_elu, 2)} kN\n")

            if "cote_poteau" in donnees:
                fichier.write(f"Cote poteau : {donnees['cote_poteau']} cm\n")
                fichier.write(f"Cote semelle : {round(donnees['cote_semelle'], 2)} m\n")

        if "volume" in projet:
            fichier.write("\n--- ESTIMATION FINANCIERE ---\n")
            fichier.write(f"Volume total de beton : {round(projet['volume'], 3)} m3\n")
            fichier.write(f"Montant total du devis : {round(projet['montant'])} FCFA\n")

    print("Rapport exporte avec succes dans 'rapport.txt'.")