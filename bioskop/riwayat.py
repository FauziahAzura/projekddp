# import streamlit as st
# from beli_tiket import get_riwayat

# def show_riwayat():
#     st.title("Riwayat Pembelian Tiket")
#     riwayat = get_riwayat()
    
#     if not riwayat:  # Kondisi if-else
#         st.write("Belum ada riwayat pembelian.")
#     else:
#         for pembelian in riwayat:  # Perulangan for
#             st.subheader(f"Film: {pembelian['film']}")
#             st.write(f"Jumlah Tiket: {pembelian['jumlah']}")
#             st.write(f"Total Harga: Rp{pembelian['total']}")
#             st.write("---")

# import streamlit as st
# from beli_tiket import get_riwayat

# def show_riwayat():
#     st.title("Riwayat Pembelian Tiket")
#     riwayat = get_riwayat()

#     if not riwayat:  # Kondisi if-else
#         st.write("Belum ada riwayat pembelian.")
#     else:
#         for idx, pembelian in enumerate(riwayat):  # Perulangan for
#             st.write("🎟️" * 30)  # Garis dekorasi dengan ikon tiket
#             st.subheader(f"Struk Pembelian #{idx + 1}")
#             st.text(f"""
#             ---------------------------------
#                     **TIKET BIOSKOP**
#             ---------------------------------
#             🎬 Film        : {pembelian['film']}
#             🎟️ Jumlah Tiket: {pembelian['jumlah']}
#             🎁 Bonus Tiket : {pembelian['bonus']}
#             🎟️ Total Tiket : {pembelian['total_tiket']}
#             💳 Total Harga : Rp{pembelian['total']}
#             ---------------------------------
#             """)
#             st.write("🎟️" * 30)  # Garis dekorasi dengan ikon tiket
#             st.write("")  # Baris kosong untuk spasi


# import streamlit as st
# from beli_tiket import get_riwayat

# def show_riwayat():
#     st.title("Riwayat Pembelian Tiket")
#     riwayat = get_riwayat()
    
#     if not riwayat:  # Kondisi if-else
#         st.write("Belum ada riwayat pembelian.")
#     else:
#         for idx, pembelian in enumerate(riwayat):  # Perulangan for
#             st.write("🎟️" * 30)  # Garis dekorasi
#             st.subheader(f"Struk Tiket #{idx + 1}")
#             st.write(f"""
#             ---------------------------------
#                   **TIKET BIOSKOP**
#             ---------------------------------
#             🎬 **Film**        : {pembelian['film']}
#             📅 **Tanggal/Waktu**: {pembelian['waktu']}
#             🎟️ **Jumlah Tiket**: {pembelian['jumlah']} (Bonus: {pembelian['bonus']})
#             📍 **Baris/Kursi** : {', '.join(pembelian['seats'])}
#             💳 **Total Harga** : Rp{pembelian['total']}
#             ---------------------------------
#             """)
#             st.write("🎟️" * 30)

import streamlit as st
from beli_tiket import get_riwayat

def show_riwayat():
    st.title("🎟️ Riwayat Pembelian Tiket")
    riwayat = get_riwayat()
    
    if not riwayat:  # Jika riwayat kosong
        st.warning("Belum ada riwayat pembelian tiket.")
    else:
        for idx, pembelian in enumerate(riwayat):  # Iterasi untuk setiap pembelian
            st.write(f"### Struk Tiket #{idx + 1}")
            st.write("**🎬 Film:**", pembelian['film'])
            st.write("**📅 Tanggal/Waktu:**", pembelian['waktu'])
            st.write("**🎟️ Jumlah Tiket:**", pembelian['jumlah'], f"(Bonus: {pembelian['bonus']})")
            st.write("**📍 Kursi:**", ", ".join(pembelian['seats']))
            st.write("**💳 Total Harga:** Rp", pembelian['total'])
            st.markdown("---")  # Garis pemisah antar tiket
