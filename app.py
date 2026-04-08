import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bet261 AI Gold", layout="wide")

st.title("⚽ Bet261 Algorithm Predictor")
st.markdown("---")

# SAISIE DES DONNÉES
st.sidebar.header("📥 Données du Live")
scores_raw = st.sidebar.text_input("5 derniers scores (ex: 1-0, 2-1...)", "0-0, 0-0, 0-0, 0-0, 0-0")
equipe_a = st.sidebar.text_input("Domicile", "London Reds")
equipe_b = st.sidebar.text_input("Extérieur", "Liverpool")
cote_a = st.sidebar.number_input("Cote Domicile", value=2.10)

# LOGIQUE DE L'ALGORITHME
def calculer_vibration(scores):
    buts = []
    for s in scores.split(','):
        try:
            parts = s.strip().split('-')
            buts.append(int(parts[0]) + int(parts[1]))
        except: continue
    return sum(buts) / len(buts) if buts else 0

if st.sidebar.button("🚀 LANCER L'ANALYSE"):
    vib = calculer_vibration(scores_raw)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Vibration de la Ligue", f"{vib:.2f} buts/match")
        if vib > 2.8:
            st.error("⚠️ CYCLE SATURÉ : Attention, les prochains matchs risquent d'être pauvres en buts.")
        elif vib < 1.5:
            st.success("🔥 CYCLE CHAUD : L'algorithme va probablement libérer des buts bientôt.")
        else:
            st.info("⚖️ CYCLE NEUTRE : Suivez la hiérarchie du classement.")

    with col2:
        st.subheader("🎯 Pronostic Final")
        if "London Reds" in equipe_a and vib < 2.5:
            st.write(f"**CONSEIL :** Victoire {equipe_a} (Confiance 85%)")
        else:
            st.write("**CONSEIL :** Double Chance (1X ou X2) ou Moins de 3.5 buts")
