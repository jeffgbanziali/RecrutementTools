import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st

# Chargement des données
def load_data():
    data = pd.read_csv("./Fichiers/Data.csv", delimiter=';', header=0, encoding='latin1')
    return data

# Fonction pour prétraiter les données
def preprocess_data(data):
    data.dropna(inplace=True)
    data.drop(columns=['date'], inplace=True)
    data = pd.get_dummies(data, columns=['couleur des yeux', 'sexe', 'diplome', 'métier', 'dispo'])
    return data

# Fonction pour diviser les données en ensembles d'entraînement et de test
def split_data(data):
    X = data.drop(columns=['embauche'])
    y = data['embauche']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Fonction pour entraîner le modèle
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Chargement des données
data = load_data()

# Prétraitement des données
data = preprocess_data(data)

# Division des données
X_train, X_test, y_train, y_test = split_data(data)

# Entraînement de notre modèle
model = train_model(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)  # Probabilités des classes prédites

# Calcul l'accuracy du modèle
accuracy = accuracy_score(y_test, y_pred)

# Calcul le rapport de classification
classification_rep = classification_report(y_test, y_pred)

# Affichage des résultats de la prédiction dans un tableau avec les pourcentages de chances
results = pd.DataFrame({"Prédiction": y_pred, "Chances Recrutement": y_pred_proba[:, 1]})

# Affichage de l'accuracy du modèle et le rapport de classification
st.write("Accuracy du modèle :", accuracy)
st.write("Rapport de classification :")
st.write(classification_rep)

# Affichage des résultats de la prédiction
st.write("Résultats de la prédiction :")
st.write(results)

# Extrait les importances des variables du modèle
importances = model.feature_importances_

# Création d'un DataFrame pour afficher les importances des variables
feature_importances_df = pd.DataFrame({"Variable": X_train.columns, "Importance": importances})

# Il trie les variables par ordre d'importance décroissante
feature_importances_df = feature_importances_df.sort_values(by="Importance", ascending=False)

# Affichage des variables les plus importantes
st.write("Variables les plus importantes :")
st.write(feature_importances_df)
