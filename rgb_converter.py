import streamlit as st
import pandas as pd

# get dy Data (HS Feed)
url = "https://cdn.ullapopken.de/data/rgb_val/hs_basefile.csv"
dy_feed = pd.read_csv(url, sep=";", engine="python")

st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="https://images.ullapopken.de/cms/alle/logos/happysize/brands/_y/brand_ulla_popken_500y_white.svg" 
             width="200">
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.write("")
st.title("Artikelnummer to RGB-Identifier")
st.text("Dieser Converter gibt dir zu einen Artikelnummern den Kategorie Link mit den entsprechenden RGB-Identifiern.\nNutze die erstellte URL um dynamische Artikelpushes auf PLPs zu erstellen.")
st.write("")
# Eingabefeld (mehrzeilig)
eingabe_url = st.text_input("PLP URL:")

# Eingabefeld (mehrzeilig)
eingabe_pn = st.text_area("Artikelnummern:")

# Wenn Button gedrückt wird:
if st.button("convert"):
    st.write("")
    st.write("")
    # Hier kommt deine Logik hin:
    vals = eingabe_pn.split("\n")
    subset = dy_feed[dy_feed['ProductNumber'].isin(vals)]
    group_ids = subset['group_id'].tolist()
    output = "&pushedArticleIds=" + "&pushedArticleIds=".join(group_ids)
    ergebnis = f"{eingabe_url}{output}"
    st.text_area("Ausgabe:", value=ergebnis, height=150)

    st.write("")
    st.text("Vorschau der Artikel:")
    image_urls = subset['image_url'].tolist()
    cols = st.columns(len(image_urls))
    for col, url in zip(cols, image_urls):
        with col:
            st.markdown("<div style='padding: 0 10px; display:flex; justify-content:center;'>", unsafe_allow_html=True)
            st.image(url)
            st.markdown("</div>", unsafe_allow_html=True)

