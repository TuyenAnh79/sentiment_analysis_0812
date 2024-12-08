import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def generate_wordcloud_and_top_words(text, stopwords=None, slider_key="slider"):
    """
    Tạo Word Cloud và trả về từ điển chứa các từ phổ biến nhất.
    """
    # Tính tần suất từ
    words = text.split()
    word_counts = Counter(words)

    # Loại bỏ stopwords (nếu có)
    if stopwords:
        word_counts = Counter({word: count for word, count in word_counts.items() if word not in stopwords})

    # Chỉ giữ lại các từ phổ biến nhất thông qua slider (thêm key để tránh lỗi)
    num_words = st.slider("Chọn số lượng từ phổ biến để hiển thị", min_value=5, max_value=50, value=10, step=1, key=slider_key)
    top_words = word_counts.most_common(num_words)
    top_words_dict = dict(top_words)

    # Trả về Word Cloud và danh sách top từ phổ biến
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_words_dict)
    return wordcloud, top_words


# POSITIVE
st.subheader("Word Cloud và Top Từ POSITIVE Phổ Biến")

try:
    with open("positive_words_VN.txt", 'r', encoding='utf-8') as f:
        text_positive = f.read()
except FileNotFoundError:
    st.error("Không tìm thấy file 'positive_words_VN.txt'.")

# Gọi hàm và chia tab
wordcloud_positive, top_words_positive = generate_wordcloud_and_top_words(text_positive, slider_key="slider_positive")
tab1_positive, tab2_positive = st.tabs(["Word Cloud POSITIVE", "Top Từ Phổ Biến POSITIVE"])

with tab1_positive:
    st.write("### Word Cloud POSITIVE")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud_positive, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

with tab2_positive:
    st.write("### Top Từ POSITIVE Phổ Biến")
    for word, count in top_words_positive:
        st.write(f"{word}: {count}")

# NEGATIVE
st.subheader("Word Cloud và Top Từ NEGATIVE Phổ Biến")

try:
    with open("negative_words_VN.txt", 'r', encoding='utf-8') as f:
        text_negative = f.read()
except FileNotFoundError:
    st.error("Không tìm thấy file 'negative_words_VN.txt'.")

# Gọi hàm và chia tab
wordcloud_negative, top_words_negative = generate_wordcloud_and_top_words(text_negative, slider_key="slider_negative")
tab1_negative, tab2_negative = st.tabs(["Word Cloud NEGATIVE", "Top Từ Phổ Biến NEGATIVE"])

with tab1_negative:
    st.write("### Word Cloud NEGATIVE")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud_negative, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

with tab2_negative:
    st.write("### Top Từ NEGATIVE Phổ Biến")
    for word, count in top_words_negative:
        st.write(f"{word}: {count}")

