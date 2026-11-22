def calculer_n_elu(G, Q):
    return 1.35 * G + 1.5 * Q


def calculer_n_els(G, Q):
    return G + Q


def calculer_poteau(projet):
    """Calcule la charge ELU de chaque type de poteau."""

    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    for type_poteau, donnees in projet["poteaux"].items():

        n_elu = calculer_n_elu(donnees["G"], donnees["Q"])

        print(f"\nPoteau : {type_poteau}")
        print(f"Charge ELU : {round(n_elu, 2)} kN")


def descente_charges(projet):
    """Affiche les charges de chaque type de poteau."""

    if not projet:
        print("Veuillez d'abord saisir ou charger un projet.")
        return

    total = 0

    print("\n===== DESCENTE DE CHARGES =====")

    for type_poteau, donnees in projet["poteaux"].items():

        G = donnees["G"]
        Q = donnees["Q"]
        nombre = donnees["nombre"]

        n_elu = calculer_n_elu(G, Q)
        n_els = calculer_n_els(G, Q)

        charge_totale = n_elu * nombre
        total += charge_totale

        print(f"\nPoteau : {type_poteau}")
        print(f"Nombre : {nombre}")
        print(f"G : {G} kN")
        print(f"Q : {Q} kN")
        print(f"N_ELU : {round(n_elu, 2)} kN")
        print(f"N_ELS : {round(n_els, 2)} kN")
        print(f"Charge totale : {round(charge_totale, 2)} kN")

    print("\nCharge totale du projet :", round(total, 2), "kN")