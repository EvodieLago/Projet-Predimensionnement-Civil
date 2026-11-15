def calculer_n_elu(g, q):
    """Calcule l'effort normal ultime N_ELU = 1.35*G + 1.50*Q."""
    return 1.35 * g + 1.50 * q

def calculer_poteau(projet):
    """Calcule N_ELU et la section théorique pour chaque type de poteau."""
    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    for type_poteau, donnees in projet["poteaux"].items():
        n_elu = calculer_n_elu(donnees["G"], donnees["Q"])
        section = n_elu / 10000

        donnees["N_ELU"] = n_elu
        donnees["section"] = section

        print(f"\nPoteau : {type_poteau}")
        print(f"N_ELU : {round(n_elu, 2)} kN")
        print(f"Section minimale : {round(section, 4)} m2")

def descente_charges(projet):
    """Calcule et affiche la descente de charges globale du bâtiment."""
    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    total = 0
    for type_poteau, donnees in projet["poteaux"].items():
        n_elu = calculer_n_elu(donnees["G"], donnees["Q"])
        charge = n_elu * donnees["nombre"]
        total += charge

        print(f"\nPoteau : {type_poteau}")
        print(f"Charge unitaire (N_ELU) : {round(n_elu, 2)} kN")
        print(f"Charge totale ({donnees['nombre']} poteaux) : {round(charge, 2)} kN")

    print(f"\n>>> CHARGE TOTALE DU PROJET : {round(total, 2)} kN")