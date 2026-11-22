import math
from charge import calculer_n_elu, calculer_n_els


def predimensionner(projet):
    """Calcule les dimensions des poteaux et des semelles."""

    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return None

    resultats = {}

    for type_poteau, donnees in projet["poteaux"].items():

        G = donnees["G"]
        Q = donnees["Q"]

        # Predimensionnement du poteau
        n_elu = calculer_n_elu(G, Q)

        section = n_elu / 10000

        cote_cm = math.sqrt(section) * 100

        cote_poteau = max(20, math.ceil(cote_cm / 5) * 5)

        # Predimensionnement de la semelle
        n_els = calculer_n_els(G, Q)

        surface_semelle = n_els / 187.5

        cote_semelle = math.sqrt(surface_semelle)

        cote_semelle = math.ceil(cote_semelle / 0.05 - 1e-10) * 0.05

        # Enregistrement des resultats
        donnees["N_ELU"] = n_elu
        donnees["A_min"] = section
        donnees["cote_poteau"] = cote_poteau
        donnees["N_ELS"] = n_els
        donnees["surface_semelle"] = surface_semelle
        donnees["cote_semelle"] = cote_semelle

        resultats[type_poteau] = donnees

        # Affichage
        print(f"\n--- Poteau {type_poteau} ---")

        print(f"N_ELU : {n_elu:.2f} kN")
        print(f"Section minimale : {section:.4f} m2")
        print(f"Cote calcule : {cote_cm:.2f} cm")
        print(f"Cote retenu : {cote_poteau} cm")

        print(f"\nN_ELS : {n_els:.2f} kN")
        print(f"Surface semelle : {surface_semelle:.3f} m2")
        print(f"Cote semelle retenu : {cote_semelle:.2f} m")

    return resultats