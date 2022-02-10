import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from dataframe import load_data


data = load_data()

def app():
    st.title('Hypothesis Testing')
    st.markdown('showing hypothesis testing using ANOVA')

    st.write("""
    
    Based on data exploration, i will use Total for creating hypothesis testing for each invidual branch. I assume Total can be known as sales daily based on date

    These are my hypothesis based on average sales (Total) from each branch:

    ***H0: μ_A = μ_B = μ_C***

    ***H1: μ_A != μ_B != μ_C***
    
    
    """)

    radio_button=st.radio("Pilih visualisasi", ("Jangan Tampilkan Visualisasi", "Grafik beberapa kategori berdasarkan Total"))
    if radio_button == 'Jangan Tampilkan Visualisasi':
        st.empty()
    elif radio_button == 'Grafik beberapa kategori berdasarkan Total':
            df_can_col = st.selectbox("Pilih Data Total sales Berdasarkan Kategori", ['Gender', 'Payment', 'Customer Type', 'Product Line'])
            if df_can_col == 'Payment':
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="total", hue='payment', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total ");
                    st.pyplot(g)
            elif df_can_col == 'Gender':
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="total", hue='gender', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total");
                    st.pyplot(g)
            elif df_can_col == 'Customer Type':
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="total", hue='customer_type', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total");
                    st.pyplot(g)
            else:
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="total", hue='product_line', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total");
                    st.pyplot(g)


    radio_button_p_value=st.radio("Pilih nilai", ("lihat daily average total", "lihat p_value"))

    if radio_button_p_value == "lihat daily average total":
        st.set_option('deprecation.showPyplotGlobalUse', False)
        data_a = data[data['branch']=='A'].groupby('date').sum()['quantity']
        data_b = data[data['branch']=='B'].groupby('date').sum()['quantity']
        data_c = data[data['branch']=='C'].groupby('date').sum()['quantity']
        st.write("Daily Average total A: ",data_a.mean())
        st.write("Daily Average total B: ",data_b.mean())
        st.write("Daily Average total C: ",data_c.mean())
    else:
        st.write('P_value: 0.9798700751931285')


    st.write("""
    
   p_value 0.9798700751931285 is bigger than ciritical value which mean H0 should be accepted and H1 should be rejected, which mean total sales for each branch is not significantly different
    
    
    """)

