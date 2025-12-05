import streamlit as st
import pandas as pd
import requests
import math
from requests.auth import HTTPBasicAuth


# KONFIG
st.set_page_config(page_title="Onsite Toolstack", layout="wide")

# --- Navigation ---
page = st.sidebar.radio("Navigation", ["Start", "Dynamischer Artikelpush", "FFNG Crawler - Artikel", "FFNG Crawler - Shops", "FFNG Crawler - Search", "Artikel Abfrage"], width=400)

if page == "Start":
    st.title("Startseite")
    st.write("Willkommen in der App!")
    st.write("Du befindest dich im Onsite Toolstack. Hier findest folgende Tools:")
    df = pd.DataFrame({"Tool": ["Dynamischer Artikelpush", "FF Crawler - Artikel", "FF Crawler - Shops", "FF Crawler - Search"], "Beschreibung/Funktion": ["Erstelle dir einen Link, welcher auf eine PLP mit gespushten Produkten verweist.", "Frage für eineen bestimmten Shop eine Kampagne ab. Output: Artikelnummern und Anzahl an Artikeln der Kampagne.", "Frage für alle Shops eine Kampagne ab und bekomme die jeweilige Anzahl der Artikel wieder.", "Frage für einen bestimmten Shop einen Suchbegriff ab. Output: Artikelnummern und Anzahl an Artikeln des Suchbegriffs."]})
    st.dataframe(
        df,
        column_config={
            "Tool": st.column_config.TextColumn("Tool", width="small"),
            "Beschreibung/Funktion": st.column_config.TextColumn(
                "Beschreibung / Funktion", width="large"
            ),
        },
        hide_index=True,
    )
