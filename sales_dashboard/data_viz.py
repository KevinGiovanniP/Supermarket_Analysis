from select import select
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from dataframe import load_data


data = load_data()



def app():
    st.title('Sales Data Visualization')
    st.markdown('data transaksi supermarket dalam 3 bulan untuk 3 cabang')

    agree = st.checkbox('Lihat Data')

    if agree:
        st.write(data.head(10))


    
    col1, col2 = st.columns(2)
    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Jumlah transaksi terbanyak berdasarkan cabang")
        sns.countplot(data['branch'])
        data['branch'].value_counts
        plt.title("Total sale setiap hari di setiap cabang")
        st.pyplot()

    with col2:
        st.subheader("Jumlah pengunjung supermarket berdasarkan gender")
        sns.countplot(x ='branch', hue='gender', palette = 'flare', data=data)
        plt.xlabel("Day")
        plt.title("Jumlah pengunjung di setiap cabang")
        st.pyplot()

    df_perbadingan_total = st.selectbox("Pilih grafik", ['kuantitas produk terbanyak', 'korelasi antar parameter',' perbandingan data rating untuk tiap jenis produk '])
    
    if df_perbadingan_total == 'kuantitas produk terbanyak':
        st.subheader("Jumlah pembelian produk paling banyak")
        xdata = [1,2,3,4,5,6,7,8,9,10]
        plt.figure(figsize = (12,6))
        sns.distplot(data['quantity'])
        plt.xticks(xdata)
        st.pyplot()
        st.write('berdasarkan grafik dapat dilihat bahwa customer paling banyak membeli 10 buah produk')
    elif df_perbadingan_total == 'korelasi antar parameter':
        st.subheader("korelasi antar parameter dataset ")
        sns.heatmap(np.round(data.corr(),2), annot=True)
        st.pyplot()
        st.write('angka 1 menandakan parameter saling berkorelasi sendangkan minus memiliki arti bahwa parameter tidak saling berkorelasi')
    else:
        xdata = [0,1,2,3,4,5,6,7,8,9,10]
        plt.figure(figsize = (12,6))
        sns.barplot(y = data['product_line'], x = data['rating'])
        plt.xticks(xdata)
        st.pyplot()
        st.write("terlihat bahwa rating tiap jenis product tidak berbeda jauh")


