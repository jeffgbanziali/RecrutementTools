# Analyse Exploratoire des Données (EDA)

Ce script Python effectue une analyse exploratoire des données (EDA) sur les données de recrutement de l'entreprise CANDI-DATA.



## Packages Utilisés
Le script utilise les packages suivants :
- pandas : Pour la manipulation et l'analyse des données.
- seaborn : Pour la création de graphiques statistiques.
- matplotlib.pyplot : Pour la création de graphiques personnalisés.
- scipy.stats : Pour effectuer le test de chi2 pour évaluer la dépendance entre les variables catégorielles.
- streamlit : Pour créer une interface utilisateur pour afficher les résultats.

## Chargement des Données

Les données sont chargées à partir du fichier Data.csv, qui contient l'historique de recrutement de l'entreprise.

## Exploration des Données

Nous avons affiché les premières lignes des données ainsi que des informations générales sur celles-ci.

## Graphiques Exploratoires

Nous avons généré plusieurs graphiques pour explorer la relation entre différentes variables et le processus d'embauche :

1. **Distribution de l'embauche :** Un graphique en barres montrant la répartition des embauches.
2. **Relation entre le sexe et l'embauche :** Un graphique en barres montrant la relation entre le sexe des candidats et leur embauche.
3. **Relation entre le métier et l'embauche :** Un graphique en barres montrant la relation entre le métier des candidats et leur embauche.
4. **Test de Chi2 pour la dépendance entre le sexe et le métier :** Nous avons effectué un test de Chi2 pour évaluer la dépendance entre le sexe et le métier des candidats.


5. **Relation entre le salaire demandé et la couleur des yeux :** Un graphique en boîte montrant la relation entre le salaire demandé par les candidats et la couleur de leurs yeux.

6. **Relation entre le nombre d'années d'expérience et la note du test technique :** Un graphique en nuage de points montrant la relation entre le nombre d'années d'expérience professionnelle des candidats et leur note au test technique.

## Synthèse des Analyses

Nous avons résumé les principales conclusions de notre analyse dans le cadre de l’audit interne.

## Exécution du Script avec Streamlit

# Pour afficher les graphiques, exécutez ce script et ouvrez le navigateur sur l'URL générée par Streamlit.
Pour exécuter le script Python avec Streamlit, assurez-vous d'avoir les bibliothèques nécessaires installées. Ensuite, vous pouvez exécuter le script à l'aide de la commande suivante :

```bash
streamlit run audit_interne.py
