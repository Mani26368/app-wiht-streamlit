import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Titre de l'app ---
st.title("📊 Dashboard de Ventes")
st.write("Bienvenue sur mon application de visualisation de données !")

# --- Génération de données fictives ---
np.random.seed(42)
mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", 
        "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]
ventes = np.random.randint(5000, 20000, size=12)
depenses = np.random.randint(3000, 12000, size=12)

df = pd.DataFrame({
    "Mois": mois,
    "Ventes": ventes,
    "Dépenses": depenses,
    "Profit": ventes - depenses
})

# --- Afficher le tableau ---
st.subheader("📋 Tableau des données")
st.dataframe(df)

# --- Graphique en barres ---
st.subheader("📈 Ventes et Dépenses par mois")
fig, ax = plt.subplots(figsize=(10, 4))
x = np.arange(len(mois))
ax.bar(x - 0.2, ventes, width=0.4, label="Ventes", color="steelblue")
ax.bar(x + 0.2, depenses, width=0.4, label="Dépenses", color="tomato")
ax.set_xticks(x)
ax.set_xticklabels(mois)
ax.legend()
st.pyplot(fig)

# --- Graphique courbe profit ---
st.subheader("💰 Évolution du Profit")
st.line_chart(df.set_index("Mois")["Profit"])

# --- Filtre interactif ---
st.subheader("🔍 Explorer par mois")
mois_choisi = st.selectbox("Choisis un mois :", mois)
ligne = df[df["Mois"] == mois_choisi].iloc[0]
st.metric("Ventes", f"{ligne['Ventes']} €")
st.metric("Dépenses", f"{ligne['Dépenses']} €")
st.metric("Profit", f"{ligne['Profit']} €")
