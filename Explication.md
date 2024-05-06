# Explication des Cas d'Utilisation des Fichiers .ipynb et .py

Ce projet utilise à la fois des fichiers .ipynb (Notebook Jupyter) et des fichiers .py (scripts Python) pour répondre aux exigences du Test Technique du Crédit Agricole Brie Picardie (CABP).

## Cas d'Utilisation du Fichier .ipynb

Le fichier .ipynb est utilisé pour l'analyse exploratoire des données (Partie 1) et pour la construction du modèle de prédiction (Partie 2). Voici comment chaque partie utilise le fichier .ipynb :

### Partie 1: Audit Interne

Le fichier `audit_interne.ipynb` contient le code et les analyses pour l'audit interne. Il explore les données de recrutement fournies par le CABP et effectue diverses analyses pour évaluer l'objectivité des processus de recrutement. Les résultats de l'audit sont présentés dans le notebook.

### Partie 2: Construction du Modèle

Le fichier `modele_construction.ipynb` est utilisé pour construire un modèle de prédiction basé sur les données de recrutement. Il utilise les techniques de machine learning pour entraîner un modèle capable de prédire si un candidat sera recruté ou non. Les détails sur la construction du modèle sont présentés dans le notebook.

## Cas d'Utilisation du Fichier .py avec l'utilisation du package Streamlit pour le rendu visuel

Les fichiers .py sont utilisés de la même manière que les fichiers .ipynb, mais ils fournissent une alternative pour exécuter le code en dehors de l'environnement Jupyter. De plus, dans le cas des fichiers .py, le package Streamlit est utilisé pour créer une interface utilisateur web conviviale pour visualiser les résultats.

### Partie 1: Audit Interne

Le fichier `audit_interne.py` contient le même code que `audit_interne.ipynb`, mais sous forme de script Python. Il peut être exécuté à partir d'un terminal ou d'un environnement de développement Python standard pour effectuer l'audit interne. L'utilisation de Streamlit permet de visualiser les graphiques et les résultats dans une interface web interactive.

### Partie 2: Construction du Modèle

Le fichier `modele_construction.py` est similaire à `modele_construction.ipynb`, mais il est écrit sous forme de script Python. Il peut être exécuté pour construire et entraîner le modèle de prédiction en dehors de l'environnement Jupyter. L'utilisation de Streamlit permet également de visualiser les résultats du modèle de manière conviviale dans une interface web.

