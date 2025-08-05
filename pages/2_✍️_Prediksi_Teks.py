import streamlit as st
import re
import string
import pickle
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk

# ——— Hindari error punkt_tab dengan mengganti tokenizer ———
# Tetap download stopwords
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

# ——— Streamlit Config ———
st.set_page_config(
    page_title="Shopee Sentiment Analysis",
    page_icon="img/mzn.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.image("img/ath2.png")
st.title("🔍 Prediction Shopee Sentiment Analysis")
st.markdown("<br>", unsafe_allow_html=True)

# ——— Load Model & TF-IDF ———
with open('model_nb.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# ——— Preprocessing Functions ———
def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#[A-Za-z0-9]+', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r'[0-9]+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace('\n', ' ')
    return text.translate(str.maketrans('', '', string.punctuation)).strip()

def casefoldingText(text):
    return text.lower()

def tokenizingText(text):
    return text.split()  # Ganti word_tokenize dengan split()

def filteringText(tokens):
    stopwords_id = set(stopwords.words('indonesian'))
    stopwords_en = set(stopwords.words('english'))
    custom_stopwords = {'iya','yaa','gak','nya','na','sih','ku','di','ga','ya','gaa','loh','kah','woi','woii','woy'}
    all_stopwords = stopwords_id | stopwords_en | custom_stopwords
    return [w for w in tokens if w not in all_stopwords]

def stemmingText(text):
    stemmer = StemmerFactory().create_stemmer()
    return ' '.join(stemmer.stem(w) for w in text.split())

def preprocessing_lengkap(text):
    text = cleaningText(text)
    text = casefoldingText(text)
    tokens = tokenizingText(text)
    filtered = filteringText(tokens)
    filtered_text = ' '.join(filtered)
    return stemmingText(filtered_text)

# ——— Input dan Prediksi ———
text = st.text_input("Masukkan kalimat ulasan:")

if st.button("Prediksi Sentimen"):
    if not text.strip():
        st.warning("Silakan masukkan kalimat terlebih dahulu.")
    else:
        preprocessed = preprocessing_lengkap(text)
        vector = tfidf.transform([preprocessed])
        prediction = model.predict(vector)[0]

        if prediction in ('positive', 'positif'):
            st.markdown("<h1 style='text-align:center;color:green;'>Positive Sentiment</h1>", unsafe_allow_html=True)
            st.columns(3)[1].image("img/positive_ils.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center;color:red;'>Negative Sentiment</h1>", unsafe_allow_html=True)
            st.columns(3)[1].image("img/negative_ils.png", use_container_width=True)
