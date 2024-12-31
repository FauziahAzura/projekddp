import streamlit as st
import base64
from home import show_home
from jadwal_film import show_jadwal_film
from beli_tiket import show_beli_tiket
from riwayat import show_riwayat

st.set_page_config(page_title="Sistem Penjualan Tiket Bioskop", layout="wide")

# Fungsi untuk menambahkan gaya CSS dari gambar lokal
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        b64_image = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{b64_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Panggil fungsi untuk menambahkan background
add_bg_from_local("bg.jpg")

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

