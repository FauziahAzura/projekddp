import streamlit as st

# Data film menggunakan class
class Film:
    def __init__(self, judul, jam, harga, gambar, tempat):
        self.judul = judul
        self.jam = jam
        self.harga = harga
        self.gambar = gambar
        self.tempat = tempat

# Daftar film
jadwal_film = [
    Film("AVENGERS: ENDGAME", "19:00", 50000, "assets/Avengers.jpg", "Theatre 1"),
    Film("Bila Esok IBU TIADA", "21:00", 45000, "assets/BilaEsokIbuTiada.jpg", "Theatre 2"),
    Film("Pamali: DUSUN POCONG", "18:30", 55000, "assets/pamali.jpg", "Theatre 3"),
    Film("2nd Miracle In Cell No.7", "15:30", 55000, "assets/2nd Miracle In Cell No.7.jpg", "Theatre 4"),
    Film("JANJI DARAH", "12:30", 35000, "assets/Janji Darah.jpg", "Theatre 5"),
    Film("MENCURI RADEN SALEH", "16:30", 45000, "assets/MencuriRadenSaleh.jpg", "Theatre 6"),
    Film("AGAK LAEN", "18:30", 55000, "assets/AgakLaen.jpg", "Theatre 7"),
    Film("MUFASA: THE LION KING", "18:45", 50000, "assets/mufasa.jpg", "Theatre 8"),
]

def show_jadwal_film():
    # st.title("Jadwal Film")
    st.markdown('<div class="title">JADWAL FILM</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Berikut adalah daftar film yang tersedia:</div>', unsafe_allow_html=True)
    
    # st.write("Berikut adalah daftar film yang tersedia:")
    for film in jadwal_film:
        st.subheader(f"🎬 {film.judul}")
        st.image(film.gambar, use_container_width=True)
        st.write(f"*Jam Tayang:* {film.jam}")
        st.write(f"*Tempat:* {film.tempat}")
        st.write(f"*Harga Tiket:* Rp. {film.harga}")
        st.write("---")
    
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
    
import streamlit as st

# Data film menggunakan class
class Film:
    def __init__(self, judul, jam, harga, gambar, tempat):
        self.judul = judul
        self.jam = jam
        self.harga = harga
        self.gambar = gambar
        self.tempat = tempat
        
        
    