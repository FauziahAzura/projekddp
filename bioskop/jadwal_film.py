import streamlit as st

# Data film menggunakan class
class Film:
    def __init__(self, judul, jam, harga, gambar):
        self.judul = judul
        self.jam = jam
        self.harga = harga
        self.gambar = gambar

# Daftar film
jadwal_film = [
    Film("Avengers: Endgame", "19:00", 50000, "assets/Avengers.jpg"),
    Film("Bila Esok Ibu Tiada", "21:00", 45000, "assets/BilaEsokIbuTiada.jpg"),
    Film("Pamali: Dusun Pocong", "18:30", 55000, "assets/pamali.jpg"),
    Film("2nd Miracle In Cell No.7", "15:30", 55000, "assets/2nd Miracle In Cell No.7.jpg"),
    Film("Janji Darah", "12:30", 35000, "assets/Janji Darah.jpg"),
    Film("Mencuri Raden Sale", "16:30", 45000, "assets/MencuriRadenSaleh.jpg"),
    Film("Agak Laen", "18:30", 55000, "assets/AgakLaen.jpg"),
]

def show_jadwal_film():
    st.title("Jadwal Film")
    st.write("Berikut adalah daftar film yang tersedia:")
    for film in jadwal_film:
        st.subheader(f"🎬 {film.judul}")
        st.image(film.gambar, use_container_width=True)
        st.write(f"*Jam Tayang:* {film.jam}")
        st.write(f"*Harga Tiket:* Rp{film.harga}")
        st.write("---")
        
