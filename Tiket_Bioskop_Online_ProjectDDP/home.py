import streamlit as st

def show_home():
    # Menambahkan CSS untuk gaya dan font
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
            .caption {
                font-size: 20px;
                font-weight: bold;
                color: #3e8e41;
                text-align: center;
                margin-top: 10px;
            }
            .content {
                font-size: 18px;
                line-height: 1.6;
                text-align: center;
                color: #555;
                margin-top: 20px;
                font-family: 'Arial', sans-serif;
            }
            .content ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
            }
            .content li {
                font-size: 20px;
                margin-bottom: 10px;
            }
            
        </style>
    """, unsafe_allow_html=True)

    # Menampilkan judul dan gambar dengan desain baru
    st.markdown('<div class="title">SELAMAT DATANG DI SISTEM PENJUALAN TIKET BIOSKOP</div>', unsafe_allow_html=True)
    st.write("")
    st.write("")
    
    # Menampilkan gambar dengan caption
    st.image("filmhome.jpg", use_container_width=True)
    st.markdown('<div class="caption">Nikmati Film Favorit Anda!</div>', unsafe_allow_html=True)

    # Menampilkan teks deskripsi dengan gaya baru
    st.markdown("""
        <div class="content">
            Aplikasi ini memungkinkan Anda untuk:
            <ul>
                <li>Melihat jadwal film terbaru.</li>
                <li>Membeli tiket secara online.</li>
                <li>Mengelola riwayat pembelian tiket Anda.</li>
            </ul>
            Nikmati pengalaman menonton yang menyenangkan!
        </div>
    """, unsafe_allow_html=True)
