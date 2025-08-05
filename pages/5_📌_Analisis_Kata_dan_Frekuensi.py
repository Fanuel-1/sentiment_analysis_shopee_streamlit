import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import seaborn as sns
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Sidebar logo
st.sidebar.image("img/ath2.png")

# ========== KONFIGURASI STOPWORDS ==========
stopwords_ind = set(stopwords.words("indonesian"))

# Tambahkan stopwords khusus untuk domain e-commerce
custom_stopwords = {
    'yg', 'shopee', 'aja', 'udah', 'banget', 'tolong', 'nya', 'sih', 'deh', 
    'dong', 'ya', 'nih', 'lah', 'ku', 'mu', 'dll', 'dgn', 'dr', 'ga', 'gak', 'kasih',
    'yg', 'di', 'yg', 'ke', 'dari', 'dan', 'yang', 'dengan', 'untuk', 'pada', 'cepat',
    'juga', 'ini', 'itu', 'saja', 'saya', 'kamu', 'kami', 'kita', 'mereka', 'murah',
    'adalah', 'ada', 'akan', 'atau', 'tapi', 'jika', 'karena', 'seperti', 'gratis',
    'dalam', 'oleh', 'bisa', 'harus', 'sudah', 'belum', 'tidak', 'bukan',
    'jangan', 'apa', 'siapa', 'bagaimana', 'kenapa', 'dimana', 'kapan', 'sesuai', 'buka', 'lambat', 'bagus', 'suka','mudah'
}

# Gabungkan stopwords NLTK dengan custom stopwords
all_stopwords = stopwords_ind.union(custom_stopwords)

# ========== FUNGSI BANTU ==========
def get_meaningful_words(corpus, n=None):
    """
    Fungsi untuk mendapatkan kata-kata bermakna dengan menghilangkan:
    - Stopwords
    - Kata umum e-commerce yang tidak spesifik
    - Kata dengan panjang < 3 karakter
    """
    tokens = [
        word for text in corpus 
        for word in text.split() 
        if (word not in all_stopwords) and (len(word) > 2)
    ]
    
    # Hitung frekuensi dan filter kata yang tidak bermakna
    counter = Counter(tokens)
    meaningful_words = [word for word in counter.most_common() if word[1] > 5]  # Minimal muncul 5 kali
    
    return meaningful_words[:n]

def generate_wordcloud(text, title):
    # Filter kata tidak bermakna
    filtered_text = ' '.join([
        word for word in text.split() 
        if (word not in all_stopwords) and (len(word) > 2)
    ])
    
    wordcloud = WordCloud(
        width=800, 
        height=400, 
        background_color='white',
        stopwords=all_stopwords
    ).generate(filtered_text)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.subheader(title)
    st.pyplot(fig)

# ========== LAYOUT STREAMLIT ==========
st.set_page_config(page_title="Analisis Kata", page_icon="📌")

st.title("📌 Analisis Kata & Frekuensi")
uploaded_file = st.file_uploader("Unggah file hasil prediksi (dengan kolom 'text_akhir' dan 'hasil_prediksi')", type='csv')

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df = df.dropna(subset=['text_akhir', 'hasil_prediksi'])  # Hindari error
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        st.stop()

    st.success("File berhasil dimuat!")

    # ==== 1. Tabel kata bermakna untuk sentimen positif/negatif ====
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔵 10 Kata Bermakna - Sentimen Positif")
        pos_words = get_meaningful_words(df[df['hasil_prediksi'] == 'positive']['text_akhir'], 10)
        st.table(pd.DataFrame(pos_words, columns=['Kata', 'Frekuensi']))

    with col2:
        st.subheader("🔴 10 Kata Bermakna - Sentimen Negatif")
        neg_words = get_meaningful_words(df[df['hasil_prediksi'] == 'negative']['text_akhir'], 10)
        st.table(pd.DataFrame(neg_words, columns=['Kata', 'Frekuensi']))

    # ==== 2. Analisis Topik Berdasarkan Kata Kunci ====
    st.subheader("🔍 Analisis Topik Ulasan")
    
    # Kategori masalah berdasarkan kata kunci negatif
    negative_categories = {
        'Pengiriman': ['pengiriman', 'kurir', 'kirim', 'antar', 'terima', 'pengantaran', 'lambat', 'lama'],
        'Aplikasi': ['aplikasi', 'update', 'versi', 'bug', 'error', 'crash', 'loading', 'hang'],
        'Pembayaran': ['bayar', 'pembayaran', 'transfer', 'refund', 'diskon', 'voucher', 'cashback', 'gagal'],
        'Produk': ['barang', 'murah', 'kualitas', 'cacat', 'rusak', 'palsu', 'orisinil', 'bekas', 'beda'],
        'Layanan': ['cs', 'pelayanan', 'respon', 'komplain', 'keluhan', 'bantuan', 'tanggapan']
    }
    
    # Kategori positif berdasarkan kata kunci positif
    positive_categories = {
        'Harga': ['murah', 'terjangkau', 'harga', 'promo', 'diskon', 'cashback', 'voucher'],
        'Kualitas': ['bagus', 'berkualitas', 'asli', 'original', 'awet', 'tahan', 'premium'],
        'Pengiriman': ['cepat', 'tepat', 'aman', 'packing', 'rapi', 'protektif', 'selamat'],
        'Pengalaman': ['puas', 'senang', 'memuaskan', 'recommended', 'rekomendasi', 'terbaik'],
        'Fitur': ['fitur', 'cashback', 'game', 'voucher', 'gratis', 'ongkir', 'poin', 'hadiah']
    }
    
    # Hitung frekuensi kategori negatif
    neg_category_counts = {category: 0 for category in negative_categories}
    negative_reviews = ' '.join(df[df['hasil_prediksi'] == 'negative']['text_akhir']).split()
    
    for word in negative_reviews:
        for category, keywords in negative_categories.items():
            if word in keywords:
                neg_category_counts[category] += 1
    
    # Hitung frekuensi kategori positif
    pos_category_counts = {category: 0 for category in positive_categories}
    positive_reviews = ' '.join(df[df['hasil_prediksi'] == 'positive']['text_akhir']).split()
    
    for word in positive_reviews:
        for category, keywords in positive_categories.items():
            if word in keywords:
                pos_category_counts[category] += 1
    
    # Tampilkan hasil dalam 2 kolom
    col_neg, col_pos = st.columns(2)
    
    with col_neg:
        st.subheader("🔴 Topik Masalah")
        problem_df = pd.DataFrame({
            'Kategori': list(neg_category_counts.keys()),
            'Frekuensi': list(neg_category_counts.values())
        }).sort_values('Frekuensi', ascending=False)
        
        st.dataframe(problem_df)
        
        # Visualisasi masalah
        if problem_df['Frekuensi'].sum() > 0:
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x='Frekuensi', y='Kategori', data=problem_df, palette='Reds_r')
            ax.set_title("Distribusi Masalah")
            st.pyplot(fig)
    
    with col_pos:
        st.subheader("🔵 Topik Keunggulan")
        strength_df = pd.DataFrame({
            'Kategori': list(pos_category_counts.keys()),
            'Frekuensi': list(pos_category_counts.values())
        }).sort_values('Frekuensi', ascending=False)
        
        st.dataframe(strength_df)
        
        # Visualisasi keunggulan
        if strength_df['Frekuensi'].sum() > 0:
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x='Frekuensi', y='Kategori', data=strength_df, palette='Blues_r')
            ax.set_title("Distribusi Keunggulan")
            st.pyplot(fig)

    # ==== 3. Analisis Komparatif ====
    st.subheader("📊 Komparasi Topik Positif vs Negatif")
    
    # Gabungkan data untuk visualisasi komparatif
    comparison_data = []
    for category in set(positive_categories.keys()).union(negative_categories.keys()):
        pos_freq = pos_category_counts.get(category, 0)
        neg_freq = neg_category_counts.get(category, 0)
        if pos_freq > 0 or neg_freq > 0:
            comparison_data.append({'Kategori': category, 'Positif': pos_freq, 'Negatif': neg_freq})
    
    comparison_df = pd.DataFrame(comparison_data).set_index('Kategori')
    
    # Tampilkan tabel komparasi
    st.dataframe(comparison_df)
    
    # Visualisasi komparasi
    fig, ax = plt.subplots(figsize=(10, 6))
    comparison_df.plot(kind='barh', ax=ax, color=['#1f77b4', '#d62728'])
    ax.set_title("Perbandingan Frekuensi Topik")
    ax.set_xlabel("Frekuensi")
    ax.set_ylabel("Kategori")
    ax.legend(title='Sentimen')
    st.pyplot(fig)

    # ==== 4. Wordcloud untuk kata bermakna ====
    st.subheader("☁️ Wordcloud Kata Bermakna")
    
    col1, col2 = st.columns(2)
    with col1:
        generate_wordcloud(' '.join(df[df['hasil_prediksi'] == 'positive']['text_akhir']), 
                          "Sentimen Positif")
    
    with col2:
        generate_wordcloud(' '.join(df[df['hasil_prediksi'] == 'negative']['text_akhir']), 
                          "Sentimen Negatif")

else:
    st.info("Silakan unggah file .csv hasil prediksi sentimen terlebih dahulu.")