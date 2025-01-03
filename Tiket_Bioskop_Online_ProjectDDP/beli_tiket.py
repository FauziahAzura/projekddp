import streamlit as st
from jadwal_film import jadwal_film
import datetime

# Data riwayat pembelian
riwayat = []

def show_beli_tiket():
    # st.title("🎟️ Pembelian Tiket")
    st.markdown('<div class="title">🎟️ PEMBELIAN TIKET</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Silakan pilih film dan jumlah tiket yang ingin Anda beli</div>', unsafe_allow_html=True)
    # st.write("Silakan pilih film dan jumlah tiket yang ingin Anda beli.")

    # Dropdown pilihan film
    pilihan_film = [film.judul for film in jadwal_film]
    film_dipilih = st.selectbox("Pilih Film", pilihan_film)

    # Input jumlah tiket
    jumlah_tiket = st.number_input("Masukkan Jumlah Tiket", min_value=1, step=1)
    
    # Input row dan nomor kursi awal
    row = st.text_input("Masukkan Baris Kursi (contoh: A, B, C)", "A")
    seat_start = st.number_input("Nomor Kursi Awal", min_value=1, step=1)
    
    # Dropdown pilihan metode pembayaran
    metode_pembayaran = st.selectbox("Pilih Metode Pembayaran", ["Kartu Kredit", "Transfer Bank", "GoPay", "OVO", "Dana"])

    # Proses pembelian tiket
    if st.button("Beli Tiket"):
        # Cari data film berdasarkan judul
        film = next(f for f in jadwal_film if f.judul == film_dipilih)

        # Bonus tiket jika beli lebih dari 2
        bonus_tiket = 0
        if jumlah_tiket > 2:
            bonus_tiket = 1  # Dapat 1 tiket gratis
            st.info("🎉 Anda mendapatkan 1 tiket gratis!")

        total_tiket = jumlah_tiket + bonus_tiket
        total_harga = film.harga * jumlah_tiket  # Harga hanya dihitung untuk tiket yang dibeli

        # Waktu pembelian
        waktu_pembelian = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Nomor kursi
        seats = [f"{row}{seat_start + i}" for i in range(total_tiket)]
        
        
        # Tambahkan ke riwayat pembelian
        riwayat.append({
            "film": film_dipilih,
            "jam": film.jam,  # Tambahkan jam tayang
            "tempat": film.tempat,  # Tambahkan tempat
            "jumlah": jumlah_tiket,
            "bonus": bonus_tiket,
            "total_tiket": total_tiket,
            "total": total_harga,
            "seats": seats,
            "waktu": waktu_pembelian,
            "metode_pembayaran": metode_pembayaran
        })

        # Tampilkan ringkasan pembelian
        st.success(f"Tiket berhasil dibeli untuk film *{film_dipilih}* sebanyak *{jumlah_tiket}* tiket (+{bonus_tiket} tiket gratis).")
        st.write(f"**Total Harga:** Rp{total_harga}")
        st.write(f"**Waktu Pembelian:** {waktu_pembelian}")
        st.write(f"**Metode Pembayaran:** {metode_pembayaran}")
    st.markdown("""
        <style>
            
            .title {
                font-size: 40px;
                color: #ffffff;
                font-weight: 700;
                text-align: center;
                margin-top: 20px;
                font-family: 'Georgia', serif;
            }
            .content {
                font-size: 25px;
                font-family: 'Georgia', serif;
                font-weight: bold;
                color: #ffffff;
                text-align: left;
                margin-top: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
    
def get_riwayat():
    return riwayat

    