import streamlit as st
import pandas as pd

st.title("3D In-Vitro BD Intelligence Dashboard")

df = pd.read_csv("src/data/output/leads_scored.csv")

search = st.text_input("Search")
if search:
    df = df[df.apply(lambda r: search.lower() in r.to_string().lower(), axis=1)]

st.dataframe(df)
st.download_button("Download CSV", df.to_csv(index=False), "leads_scored.csv")