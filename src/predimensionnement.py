import math
from charge import calculer_n_elu

def predimensionner(projet):
    """Calcule les dimensions retenues des poteaux (cm) et des semelles (m)."""
    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    for type_poteau, donnees in projet["poteaux"].items():
        n_elu = calculer_n_elu(donnees["G"], donnees["Q"])
        section = n_elu / 10000
        cote_cm = math.sqrt(section) * 100
        cote_retenu = max(20, math.ceil(cote_cm / 5) * 5)

        charge_semelle = donnees["G"] + donnees["Q"]
        cote_semelle = math.sqrt(charge_semelle / 187.5)
        cote_semelle = math.ceil(cote_semelle / 0.05) * 0.05

        donnees["cote_poteau"] = cote_retenu
        donnees["cote_semelle"] = cote_semelle

        print(f"\nPoteau : {type_poteau}")
        print(f"Cote retenu du poteau : {cote_retenu} cm")
        print(f"Cote retenu de la semelle : {round(cote_semelle, 2)} m")