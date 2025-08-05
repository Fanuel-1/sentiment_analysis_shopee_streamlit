import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pickle

# Sidebar logo
st.sidebar.image("img/ath2.png")

# Load model dan vectorizer
with open('model_nb.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Fungsi prediksi
def predict_sentiment(texts):
    text_vector = tfidf.transform(texts)
    return model.predict(text_vector)

st.title("📊 Visualisasi Sentimen Ulasan")

uploaded_file = st.file_uploader("Upload file CSV untuk visualisasi (wajib ada kolom 'text_akhir')", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=',', on_bad_lines='skip', engine='python', quoting=3, encoding='utf-8')


    if 'text_akhir' not in df.columns:
        st.error("Kolom 'text_akhir' tidak ditemukan.")
    else:
        df['prediksi_sentimen'] = predict_sentiment(df['text_akhir'].astype(str))

        # Ringkasan
        st.subheader("📋 Ringkasan Sentimen")
        count_sentiment = df['prediksi_sentimen'].value_counts()
        st.write(count_sentiment)

        # Pie chart
        st.subheader("🥧 Distribusi Sentimen (Pie Chart)")
        fig1, ax1 = plt.subplots()
        ax1.pie(count_sentiment, labels=count_sentiment.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

        # Bar chart
        st.subheader("📊 Distribusi Sentimen (Bar Chart)")
        fig2, ax2 = plt.subplots()
        sns.countplot(data=df, x='prediksi_sentimen', palette='pastel', ax=ax2)
        ax2.set_xlabel("Sentimen")
        ax2.set_ylabel("Jumlah")
        st.pyplot(fig2)

        # WordCloud Positif & Negatif
        st.subheader("☁️ WordCloud per Sentimen")
        for label in ['positive', 'negative']:
            if label in df['prediksi_sentimen'].values:
                text_data = " ".join(df[df['prediksi_sentimen'] == label]['text_akhir'].astype(str))
                wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text_data)
                st.markdown(f"**WordCloud untuk Sentimen: {label.upper()}**")
                fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
                ax_wc.imshow(wordcloud, interpolation='bilinear')
                ax_wc.axis("off")
                st.pyplot(fig_wc)
