import streamlit as st

st.set_page_config(page_title="Dashboard Shopee", layout="wide")
st.title("📦 DASHBOARD SENTIMEN ANALISIS ULASAN APLIKASI SHOPEE")
st.write("Gunakan sidebar untuk memilih halaman.")

st.sidebar.image("img/ath2.png")

with st.columns(2)[0]:
    st.image("img/shopee.jpg")

st.write("""Shopee menghadapi tantangan dalam menjaga kepuasan pengguna akibat ulasan negatif di Google Play Store, yang dapat menurunkan reputasi, jumlah unduhan, dan pendapatan. Divisi pemasaran paling terdampak, Key Performance Indicator (KPI) yang harus dicapai oleh Divisi Pemasaran adalah terdiri dari 2 aspek:
1.	Rating Aplikasi di Google Play Store, KPI ini mengukur rata-rata rating yang diberikan oleh pengguna aplikasi Shopee di Google Play Store, yang mencerminkan tingkat kepuasan pengguna secara keseluruhan. Dengan menetapkan target rating minimal 4,5, Divisi Pemasaran berusaha untuk memastikan bahwa mayoritas pengguna memiliki pengalaman yang positif dengan aplikasi, yang penting untuk menarik dan mempertahankan pengguna baru. Evaluasi dilakukan setiap bulan, sehingga tim dapat segera mengambil tindakan jika ada penurunan rating yang mengindikasikan adanya masalah dalam aplikasi yang perlu segera diperbaiki.
2.	Jumlah Ulasan Positif, KPI ini mengukur persentase ulasan dengan sentimen positif dari total ulasan yang diterima di Google Play Store, yang merupakan indikator penting dari persepsi publik terhadap aplikasi Shopee. Targetnya adalah mencapai minimal 70% ulasan positif, yang menunjukkan bahwa sebagian besar pengguna merasa puas dengan aplikasi dan cenderung merekomendasikannya kepada orang lain. Evaluasi KPI ini dilakukan setiap bulan, memungkinkan Divisi Pemasaran untuk memantau tren sentimen pengguna secara real-time dan merespons dengan cepat jika terjadi peningkatan ulasan negatif, menggunakan alat seperti dashboard analisis sentimen untuk memastikan tindakan yang tepat dan akurat.
""")
with st.columns(3)[1]:
    st.image("img/review e-com.png")

st.write("""Solusi yang ditawarkan adalah dashboard analisis sentimen berbasis algoritma Naive Bayes, yang dapat mengklasifikasikan ulasan menjadi positif dan negatif secara efisien. Naive Bayes dipilih karena kecepatan, kesederhanaan, dan performanya yang unggul dibanding SVM dan Neural Network pada data teks, dengan akurasi mencapai 81,2%. Algoritma ini juga efektif menangani data besar, berdimensi tinggi, dan tidak seimbang, sehingga sangat cocok untuk analisis sentimen ulasan aplikasi.
""")