import streamlit as st
from home import show_home
from jadwal_film import show_jadwal_film
from beli_tiket import show_beli_tiket
from riwayat import show_riwayat

st.set_page_config(page_title="Sistem Penjualan Tiket Bioskop", layout="wide")

# Menu navigasi
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Jadwal Film", "Beli Tiket", "Riwayat Pembelian"])

# Kondisi untuk navigasi
if menu == "Home":
    show_home()
elif menu == "Jadwal Film":
    show_jadwal_film()
elif menu == "Beli Tiket":
    show_beli_tiket()
elif menu == "Riwayat Pembelian":
    show_riwayat()