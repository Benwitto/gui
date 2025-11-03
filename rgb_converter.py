import streamlit as st
import pandas as pd

# get dy Data (HS Feed)
#dy_feed = pd.read_csv(r"\\mftfile\Datenaustausch\onsite_marketing\tools\rgb_converter\hs_basefile.csv", sep=";", engine="python")
#dy_feed.to_csv(r"\\mftfile\Datenaustausch\onsite_marketing\tools\rgb_converter\hs_basefile.csv", sep=";", index=False)
url = "https://cdn.ullapopken.de/data/rgb_val/hs_basefile.csv"
dy_feed = pd.read_csv(url, sep=";", engine="python")

st.title("Artikelnummer to RGB-Identifier")
st.text("Dieser Converter gibt dir zu einer Artikelnummer den richtigen RGB-Identifier.\nNutze den RGB-Identifier um dynamische Artikelpushes auf PLPs zu erstellen.")

# Eingabefeld (mehrzeilig)
eingabe = st.text_area("Artikelnummern:")

# Wenn Button gedrückt wird:
if st.button("Covert ProductNumbers to RGB_IDs"):
    # Hier kommt deine Logik hin:
    vals = eingabe.split("\n")
    subset = dy_feed[dy_feed['ProductNumber'].isin(vals)]
    group_ids = subset['group_id'].tolist()
    output = "\n".join(group_ids)
    ergebnis = f"{output}"
    st.text_area("Ausgabe:", value=ergebnis, height=200)
