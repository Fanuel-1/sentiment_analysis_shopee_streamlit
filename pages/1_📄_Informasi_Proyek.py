import streamlit as st

st.title("📄 INFORMASI")

# Sidebar logo
st.sidebar.image("img/ath2.png")

st.markdown("""
### 🎯 Tujuan Proyek
Penelitian ini bertujuan untuk :
1. Mengevaluasi performa algoritma Naïve Bayes dalam mengklasifikasikan sentimen dari ulasan pengguna terhadap aplikasi Shopee di Google Play Store. Evaluasi ini dilakukan untuk menilai akurasi dan efektivitas algoritma dalam mengenali pola kata yang berkaitan dengan sentimen positif atau negatif.
2. Mengidentifikasi kata kunci atau fitur linguistik yang paling berpengaruh dalam menentukan sentimen. Kata-kata ini diharapkan menjadi indikator yang kuat terhadap kualitas layanan, pengalaman pengguna, atau keluhan yang sering muncul.
3. Mengembangkan sebuah dashboard interaktif dan informatif berbasis Streamlit yang dapat digunakan oleh pihak non-teknis (misalnya, tim pemasaran dan pengambil keputusan) untuk memahami persebaran sentimen pengguna, tren keluhan, dan faktor keberhasilan layanan secara visual dan real-time.
""")

st.markdown("""
### 🧠 Model
Model klasifikasi yang digunakan adalah Naïve Bayes, yang dikenal baik dalam tugas klasifikasi teks karena kesederhanaan dan performanya yang kompetitif pada data berukuran besar.
Pipeline proses meliputi tiga tahapan utama:

*Preprocessing Teks:*
Dilakukan pembersihan data melalui serangkaian tahapan, yaitu:
1. Cleaning (menghapus karakter non-alfabet),
2. Case Folding (mengubah semua huruf menjadi kecil),
3. Slangwords Normalization (mengubah kata tidak baku),
4. Tokenizing (memecah kalimat menjadi kata-kata),
5. Stemming (mengembalikan kata ke bentuk dasarnya),
6. Stopword Removal (menghapus kata umum yang tidak memiliki makna penting).

*Ekstraksi Fitur:*
Menggunakan pendekatan TF-IDF (Term Frequency-Inverse Document Frequency) untuk mengubah teks menjadi representasi numerik yang bisa digunakan oleh algoritma klasifikasi. Hanya 200 kata paling informatif yang dipilih untuk menghindari overfitting dan mengurangi kompleksitas komputasi.

*Klasifikasi:*
Model Naïve Bayes Multinomial diterapkan untuk melakukan prediksi sentimen. Model ini cocok untuk data diskret seperti frekuensi kata atau bobot TF-IDF.
""")

st.markdown("""
### 📊 Dataset
Dataset yang digunakan merupakan data primer yang diperoleh langsung oleh peneliti melalui proses web scraping dari halaman aplikasi Shopee di Google Play Store. Data ini mencakup:
1. Teks ulasan yang ditulis oleh pengguna,
2. Rating bintang (1–5) sebagai metadata tambahan,
3. Tanggal publikasi ulasan.
Scraping dilakukan menggunakan library Python seperti google-play-scraper. Proses ini menghasilkan data mentah yang kemudian dibersihkan dan diproses lebih lanjut sebelum digunakan dalam pelatihan model. Total ulasan yang berhasil dikumpulkan sebanyak 6000 entri, yang kemudian diproses menjadi format TF-IDF dengan 200 fitur kata.

### ✍️ Desain Penelitian
""")
st.image("img/Desain.jpg", use_container_width=True)
st.markdown("""Arsitektur ini mendukung integrasi dan pengembangan sistem secara fleksibel. Diagram tersebut menggambarkan alur pengembangan sistem kecerdasan buatan secara menyeluruh, dimulai dari pengumpulan data mentah melalui sumber seperti database atau sensor, yang kemudian diakses via Dataset API. Data dibersihkan dan dipilih fitur relevannya, lalu diproses melalui normalisasi, pengkodean, dan pembagian dataset. Data siap olah ini dimasukkan ke dalam model AI untuk pelatihan dan prediksi, lalu hasilnya disimpan dalam basis data. Pengguna berinteraksi melalui antarmuka (web, API, atau CLI) dan memantau performa lewat dasbor visual. Seluruh proses membentuk siklus otomatis yang mengubah data mentah menjadi insight siap pakai.
""")

st.markdown("""
### 👨‍💻 Fitur Aplikasi
📄 Informasi Proyek
Halaman ini berisi deskripsi tujuan proyek, metodologi penelitian, serta sumber data. Informasi ini memberikan konteks awal bagi pengguna sebelum mereka masuk ke tahap analisis teknis. Terdapat penjelasan tentang proses scraping, pembersihan data, serta alasan pemilihan model.

✏️ Prediksi Teks
Fitur ini memungkinkan pengguna untuk menginput kalimat ulasan secara langsung dan melihat hasil klasifikasinya. Sangat cocok untuk pengujian cepat terhadap satu atau dua kalimat tanpa perlu membuat file terpisah.

📁 Prediksi File
Digunakan untuk klasifikasi massal, di mana pengguna dapat mengunggah file CSV berisi banyak ulasan. Sistem akan melakukan preprocessing otomatis dan menampilkan hasil prediksi serta memberikan opsi unduh hasil dalam format CSV.

📊 Visualisasi Data
Menyajikan visualisasi berupa pie chart, bar chart, dan tabel ringkasan distribusi sentimen. Visualisasi ini memudahkan pengguna untuk melihat proporsi ulasan positif dan negatif dalam dataset dengan lebih cepat dan intuitif.

📌 Analisis Kata dan Frekuensi
Menampilkan analisis kata berdasarkan frekuensi kemunculan dalam masing-masing sentimen. Dilengkapi dengan WordCloud dan grafik batang untuk memperlihatkan kata-kata dominan dalam ulasan positif maupun negatif. Fitur ini dapat membantu tim Shopee dalam mengidentifikasi pain point dan strength point layanan mereka.
""")
