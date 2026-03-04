import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("🤖 Modèle de prédiction de fleurs")
st.write("Ce modèle prédit le type de fleur Iris selon ses caractéristiques.")

# Charger les données et entraîner le modèle
iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

# Entrées utilisateur
st.subheader("📋 Entre les caractéristiques de la fleur :")
sepal_length = st.slider("Longueur du sépale", 4.0, 8.0, 5.0)
sepal_width = st.slider("Largeur du sépale", 2.0, 5.0, 3.0)
petal_length = st.slider("Longueur du pétale", 1.0, 7.0, 4.0)
petal_width = st.slider("Largeur du pétale", 0.1, 2.5, 1.0)

# Prédiction
prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
st.subheader("🌸 Résultat :")
st.success(f"La fleur est : **{iris.target_names[prediction[0]]}**")
