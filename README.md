# Projet 1 : Cahier des charges et prédimensionnement (IIT)

Application console en Python développée dans le cadre du cours de Génie Civil & Programmation à l'Institut Ivoirien de Technologie (IIT).

## Fonctionnalités
- Saisie et sauvegarde de projet au format JSON
- Calcul des efforts à l'ELU ($N_{ELU} = 1.35G + 1.50Q$) et descente de charges
- Prédimensionnement des poteaux et des semelles isolées
- Génération automatique du devis estimatif en FCFA
- Exportation d'un rapport détaillé

## Structure du projet
- `donnees/` : Fichiers de sauvegarde JSON et bordereaux de prix
- `src/` : Code source modulaire de l'application
- `tests/` : Tests unitaires de vérification des calculs

## Lancement
```bash
python src/main.py