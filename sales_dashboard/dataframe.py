import pandas as pd
import streamlit as st


DATA_URL = 'https://raw.githubusercontent.com/KevinGiovanniP/Supermarket_Analysis/main/final_data.csv'

@st.cache
def load_data():
    dataframe = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    dataframe.rename(lowercase, axis='columns', inplace=True)
    return dataframe