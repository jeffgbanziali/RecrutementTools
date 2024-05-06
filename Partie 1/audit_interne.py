import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import streamlit as st

# Chargement des données
data = pd.read_csv("./Fichiers/Data.csv", delimiter=';', header=0, encoding='latin1')

# Exploration des données
st.write(data.head())
st.write(data.info())

# Analyse exploratoire des données (EDA)

# Distribution de l'embauche en fonction de différentes variables
fig1, ax1 = plt.subplots()
sns.countplot(x='embauche', data=data)
ax1.set_title('Distribution de l\'embauche')

# Relation entre le sexe et l'embauche
fig2, ax2 = plt.subplots()
sns.countplot(x='sexe', hue='embauche', data=data)
ax2.set_title('Relation entre le sexe et l\'embauche')

# Relation entre le métier et l'embauche
fig3, ax3 = plt.subplots()
sns.countplot(x='métier', hue='embauche', data=data)
ax3.set_title('Relation entre le métier et l\'embauche')
ax3.tick_params(axis='x', rotation=45)

# Test de chi2 pour évaluer la dépendance entre le sexe et le métier
chi2_stat, p_val, dof, expected = chi2_contingency(pd.crosstab(data['sexe'], data['métier']))
st.write("Test de Chi2 pour la dépendance entre le sexe et le métier :")
st.write("Chi2 Statistique :", chi2_stat)
st.write("P-valeur :", p_val)

# Relation entre le salaire demandé et la couleur des yeux
fig4, ax4 = plt.subplots()
sns.boxplot(x='couleur des yeux', y='salaire', data=data)
ax4.set_title('Relation entre le salaire demandé et la couleur des yeux')

# Relation entre le nombre d'années d'expérience et la note du test technique
fig5, ax5 = plt.subplots()
sns.scatterplot(x='exp', y='note', data=data)
ax5.set_title('Relation entre le nombre d\'années d\'expérience et la note du test technique')

# Affichage des graphiques dans le dashboard
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)
st.pyplot(fig4)
st.pyplot(fig5)



st.write("""
Synthèse des analyses réalisées dans le cadre de l’audit interne :

1. Distribution de l'embauche en fonction de différentes variables :
   Nous avons examiné la distribution de l'embauche en fonction du sexe et du métier des candidats. 
   Il semble y avoir des différences significatives dans l'embauche en fonction de ces variables.

2. Test de Chi2 pour la dépendance entre le sexe et le métier :
   Nous avons effectué un test de Chi2 pour évaluer la dépendance entre le sexe et le métier des candidats.
   Le test indique une dépendance statistiquement significative entre ces deux variables.

3. Relation entre le salaire demandé et la couleur des yeux :
   Nous avons examiné la relation entre le salaire demandé par les candidats et la couleur de leurs yeux.
   Aucune tendance claire n'a été observée, mais il y a eu des variations dans les salaires demandés pour différentes couleurs d'yeux.

4. Relation entre le nombre d'années d'expérience et la note du test technique :
   Nous avons tracé la relation entre le nombre d'années d'expérience professionnelle des candidats et leur note au test technique.
   Il semble y avoir une légère tendance positive entre ces deux variables, indiquant que les candidats avec plus d'expérience tendent à obtenir de meilleures notes.

Cette synthèse résume les principales conclusions de notre analyse dans le cadre de l’audit interne. 
Ces informations peuvent être utilisées pour mieux comprendre les tendances dans le processus de recrutement actuel et identifier des domaines potentiels d'amélioration.
""")

