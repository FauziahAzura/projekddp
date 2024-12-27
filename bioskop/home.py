import streamlit as st

def show_home():
    st.title("Selamat Datang di Sistem Penjualan Tiket Bioskop")
    st.image("fau.jpg", caption="Nikmati Film Favorit Anda!", use_container_width=True)
    st.write("""
        Aplikasi ini memungkinkan Anda untuk:
        - Melihat jadwal film terbaru.
        - Membeli tiket secara online.
        - Mengelola riwayat pembelian tiket Anda.

        Nikmati pengalaman menonton yang menyenangkan!
    """)