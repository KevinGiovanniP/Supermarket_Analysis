import streamlit as st
import data_viz, hypo

#st.title('Supermarket Sales Analysis')

#st.write('Historical record of sales data in 3 different supermarker branches')

#st.sidebar.file_uploader("Upload a file", type=['csv', 'txt']) 

PAGES = {
    "Data Visualization": data_viz,
    "Hypothesis Testing": hypo
}


st.sidebar.title("Menu")
selection = st.sidebar.selectbox("Pages", list(PAGES.keys()))
page = PAGES[selection]
page.app()