import app as la
import streamlit as st

st.set_page_config(layout="wide")
st.title("Company Name Generator Tabajara")

segmento = st.sidebar.text_area(label="What is the company's segment?")

if segmento:
    response = la.generate_company_name(segmento)

    st.text(response["text"])