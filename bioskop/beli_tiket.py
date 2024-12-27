# import streamlit as st
# from jadwal_film import jadwal_film

# # Data riwayat pembelian
# riwayat = []

# def show_beli_tiket():
#     st.title("Pembelian Tiket")
#     st.write("Silakan pilih film dan jumlah tiket yang ingin Anda beli.")

#     # Dropdown pilihan film
#     pilihan_film = [film.judul for film in jadwal_film]
#     film_dipilih = st.selectbox("Pilih Film", pilihan_film)

#     # Input jumlah tiket
#     jumlah_tiket = st.number_input("Masukkan Jumlah Tiket", min_value=1, step=1)

#     # Proses pembelian tiket
#     if st.button("Beli Tiket"):
#         # Cari data film berdasarkan judul
#         film = next(f for f in jadwal_film if f.judul == film_dipilih)

#         # Hitung total harga (operator *)
#         total_harga = film.harga * jumlah_tiket
        
#         # Tambahkan ke riwayat pembelian
#         riwayat.append({"film": film_dipilih, "jumlah": jumlah_tiket, "total": total_harga})
        
#         st.success(f"Tiket berhasil dibeli untuk film *{film_dipilih}* sebanyak *{jumlah_tiket}* tiket.")
#         st.write(f"*Total Harga:* Rp{total_harga}")

# def get_riwayat():
#     return riwayat

# import streamlit as st
# from jadwal_film import jadwal_film

# # Data riwayat pembelian
# riwayat = []

# def show_beli_tiket():
#     st.title("Pembelian Tiket")
#     st.write("Silakan pilih film dan jumlah tiket yang ingin Anda beli.")

#     # Dropdown pilihan film
#     pilihan_film = [film.judul for film in jadwal_film]
#     film_dipilih = st.selectbox("Pilih Film", pilihan_film)

#     # Input jumlah tiket
#     jumlah_tiket = st.number_input("Masukkan Jumlah Tiket", min_value=1, step=1)

#     # Proses pembelian tiket
#     if st.button("Beli Tiket"):
#         # Cari data film berdasarkan judul
#         film = next(f for f in jadwal_film if f.judul == film_dipilih)

#         # Hitung bonus tiket (if-else)
#         bonus_tiket = 0
#         if jumlah_tiket > 2:
#             bonus_tiket = 1  # Dapat 1 tiket gratis
#             st.info("🎉 Anda mendapatkan 1 tiket gratis!")

#         # Hitung total harga (operator *)
#         total_harga = film.harga * jumlah_tiket

#         # Total tiket termasuk bonus
#         total_tiket = jumlah_tiket + bonus_tiket

#         # Tambahkan ke riwayat pembelian
#         riwayat.append({
#             "film": film_dipilih,
#             "jumlah": jumlah_tiket,
#             "bonus": bonus_tiket,
#             "total_tiket": total_tiket,
#             "total": total_harga
#         })

#         st.success(f"Tiket berhasil dibeli untuk film *{film_dipilih}* sebanyak *{jumlah_tiket}* tiket (+{bonus_tiket} tiket gratis).")
#         st.write(f"*Total Tiket:* {total_tiket} tiket")
#         st.write(f"*Total Harga:* Rp{total_harga}")

# # Fungsi untuk mendapatkan riwayat pembelian
# def get_riwayat():
#     return riwayat

import streamlit as st
from jadwal_film import jadwal_film
import datetime

# Data riwayat pembelian
riwayat = []

def show_beli_tiket():
    st.title("Pembelian Tiket")
    st.write("Silakan pilih film dan jumlah tiket yang ingin Anda beli.")

    # Dropdown pilihan film
    pilihan_film = [film.judul for film in jadwal_film]
    film_dipilih = st.selectbox("Pilih Film", pilihan_film)

    # Input jumlah tiket
    jumlah_tiket = st.number_input("Masukkan Jumlah Tiket", min_value=1, step=1)
    
    # Input row dan seat
    row = st.text_input("Masukkan Baris Kursi (contoh: A, B, C)", "A")
    seat_start = st.number_input("Nomor Kursi Awal", min_value=1, step=1)

    # Proses pembelian tiket
    if st.button("Beli Tiket"):
        # Cari data film berdasarkan judul
        film = next(f for f in jadwal_film if f.judul == film_dipilih)

        # Hitung total harga
        total_harga = film.harga * jumlah_tiket

        # Bonus tiket jika beli lebih dari 2
        # bonus = jumlah_tiket // 3
        # total_tiket = jumlah_tiket + bonus
        bonus_tiket = 0
        if jumlah_tiket > 2:
            bonus_tiket = 1  # Dapat 1 tiket gratis
            st.info("🎉 Anda mendapatkan 1 tiket gratis!")

        total_tiket = jumlah_tiket + bonus_tiket
        
        # Waktu pembelian
        waktu_pembelian = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Nomor kursi
        seats = [f"{row}{seat_start + i}" for i in range(total_tiket)]

        # Tambahkan ke riwayat pembelian
        riwayat.append({
            "film": film_dipilih,
            "jumlah": jumlah_tiket,
            "bonus": bonus_tiket,
            "total_tiket": total_tiket,
            "total": total_harga,
            "row": row,
            "seats": seats,
            "waktu": waktu_pembelian
        })

        st.success(f"Tiket berhasil dibeli untuk film *{film_dipilih}* sebanyak *{jumlah_tiket}* tiket.")
        st.write(f"*Total Harga:* Rp{total_harga}")

def get_riwayat():
    return riwayat
