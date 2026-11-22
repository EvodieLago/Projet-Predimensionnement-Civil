from element import lire_nombre
from charge import calculer_n_elu


def generer_devis(projet):
    """Calcule le volume total de beton et genere le devis."""

    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    volume_total = 0

    for type_poteau, donnees in projet["poteaux"].items():

        if "cote_poteau" not in donnees or "cote_semelle" not in donnees:
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

    print("\n===== DEVIS ESTIMATIF =====")
    print(f"Volume total de beton : {volume_total:.3f} m3")
    print(f"Prix unitaire : {prix} FCFA")
    print(f"Montant total : {montant:.0f} FCFA")

    projet["volume"] = volume_total
    projet["montant"] = montant


def exporter_rapport(projet):
    """Exporte les resultats dans un fichier rapport.txt."""

    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    with open("rapport.txt", "w", encoding="utf-8") as fichier:

        fichier.write("=========================================\n")
        fichier.write(" RAPPORT DE PREDIMENSIONNEMENT - IIT\n")
        fichier.write("=========================================\n")

        fichier.write(f"Projet : {projet['nom']}\n")
        fichier.write(f"Hauteur : {projet['hauteur']} m\n")
        fichier.write(f"Epaisseur semelle : {projet['epaisseur']} m\n")

        for type_poteau, donnees in projet["poteaux"].items():

            n_elu = calculer_n_elu(donnees["G"], donnees["Q"])

            fichier.write(f"\n--- Poteau : {type_poteau} ---\n")
            fichier.write(f"Nombre : {donnees['nombre']}\n")
            fichier.write(f"N_ELU : {n_elu:.2f} kN\n")

            if "cote_poteau" in donnees:

                fichier.write(
                    f"Cote poteau : {donnees['cote_poteau']} cm\n"
                )

                fichier.write(
                    f"Cote semelle : {donnees['cote_semelle']:.2f} m\n"
                )

        if "volume" in projet:

            fichier.write("\n--- ESTIMATION FINANCIERE ---\n")

            fichier.write(
                f"Volume total : {projet['volume']:.3f} m3\n"
            )

            fichier.write(
                f"Montant total : {projet['montant']:.0f} FCFA\n"
            )

    print("Rapport exporte avec succes dans rapport.txt.")