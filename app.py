import streamlit as st 
from PIL import Image 

st.title ('Project Akhir Analisis Data Dengan Python')

st.header('Case')
st.text('1. Bagaimana perbandingan cnt berdasarkan season per tahunnya.')
st.text('2. Bagaimana trend dari penyewaan atau cnt berdasarkan cuaca atau weathersit.')


st.header('Case 1 ')
st.subheader('Bagaimana perbandingan cnt berdasarkan season per tahunnya')
st.image('chart1.png')
st.text('Dari visualisasi yang dihasilkan menggunakan bar chart, maka dapat disimpulkan bahwa pada setiap musim gugur penyewaan sepeda lebih tinggi dibandingkan dengan musim lainnya dan pada setiap musim semi merupakan musim dengan tingkat penyewaan paling rendah dibandingkan dengan musim lainnya')


st.header('Case 2 ')
st.subheader('Bagaimana trend dari penyewaan atau cnt berdasarkan cuaca atau weathersit')
st.image('chart2.png')
st.text('Dari visualisasi yang dihasilkan menggunakan line chart, maka dapat disimpulkan bahwa tren penyewaan sepeda per tahunnya akan mulai naik di awal tahun, kemudian rentang pada bulan 6-8 merupakan rentang bulan dengan tren penjualan tinggi yang kemudian akan mulai terjadi penurunan tren setelah bulan 8 hingga akhir tahun')


