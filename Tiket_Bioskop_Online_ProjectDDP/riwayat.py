import streamlit as st
from beli_tiket import get_riwayat

def show_riwayat():
    # st.title("🎟️ Riwayat Pembelian Tiket")
    st.markdown('<div class="title">🎟️ RIWAYAT PEMBELIAN TIKET</div>', unsafe_allow_html=True)
    riwayat = get_riwayat()  # Ambil data riwayat pembelian tiket
    
    if not riwayat:  # Jika riwayat kosong
        st.warning("Belum ada riwayat pembelian tiket.")
    else:
        for idx, pembelian in enumerate(riwayat):  # Iterasi untuk setiap pembelian
            st.subheader(f"🎫 Struk Pembelian #{idx + 1}")
            st.write("**🎬 Film:**", pembelian['film'])
            st.write("**📅 Tanggal/Waktu Pembelian:**", pembelian['waktu'])
            st.write("**🎟️ Jumlah Tiket Dibeli:**", pembelian['jumlah'], f"(Bonus: {pembelian['bonus']})")
            st.write("**💳 Total Harga:** Rp", pembelian['total'])
            
            # Tampilkan tiket sesuai jumlah tiket
            st.markdown("### 🎟️ Tiket Film")
            for i, seat in enumerate(pembelian['seats']):
                st.markdown(f"""            
                ```
                🎬 {pembelian['film']}
                -------------------------------------------------------------------------------------------------
                📅 Tanggal Pembelian: {pembelian['waktu']}
                🕒 Waktu Tayang: {pembelian['jam']}
                🏢 Tempat: {pembelian['tempat']}
                💺 Baris dan Nomor Kursi: {seat}
                ```
                """)
            st.markdown("---")  # Garis pemisah antar pembelian

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
            
        </style>
    """, unsafe_allow_html=True)
    
