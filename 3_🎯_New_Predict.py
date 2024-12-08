import pickle
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="New Predict", page_icon="🎯")

# Sidebar
st.sidebar.success("Giáo Viên Hướng Dẫn: \n # KHUẤT THUỲ PHƯƠNG")
st.sidebar.success("Học Viên:\n # NGUYỄN CHẤN NAM \n # CHẾ THỊ ANH TUYỀN")
st.sidebar.success("Ngày báo cáo: \n # 16/12/2024")

# Hàm dự đoán giá trị mới cho các bình luận
def predict_new_data_with_probabilities(model, new_texts, vectorizer):
    
    # Chuyển đổi văn bản mới thành vector
    new_texts_transformed = vectorizer.transform(new_texts)
    
    # Dự đoán xác suất cho các lớp (positive và negative)
    probabilities = model.predict_proba(new_texts_transformed)
    
    # Dự đoán nhãn cuối cùng
    predictions = model.predict(new_texts_transformed)
    
    # Kết quả: Xác suất và nhãn dự đoán
    results = []
    for text, prob, pred in zip(new_texts, probabilities, predictions):
        sentiment = "positive" if pred == 1 else "negative"
        results.append({
            "Bình luận": text,
            "Xác suất Positive": round(prob[1], 4),  # Xác suất lớp 1
            "Xác suất Negative": round(prob[0], 4),  # Xác suất lớp 0
            "Kết quả": sentiment  # Kết quả cuối cùng
        })
    return results



# Tải mô hình và vectorizer từ các file pickle
model_filename = 'svm_model.pkl'  
vectorizer_filename = 'svm_vectorizer.pkl'

# Ứng dụng Streamlit
st.title("🔮 Sentiment Prediction")
st.write("Dự đoán cảm xúc (tích cực/tiêu cực) của bình luận dựa trên mô hình học máy.")

try:
    # Tải mô hình SVM và vectorizer từ file
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)
    with open(vectorizer_filename, 'rb') as f:
        vectorizer = pickle.load(f)
    
    # Giao diện nhập dữ liệu
    st.subheader("📝 Nhập bình luận để dự đoán:")
    
    # Chọn phương thức nhập liệu: nhập tay hoặc tải file
    option = st.radio("Chọn phương pháp nhập liệu:", ["Nhập văn bản trực tiếp", "Tải file văn bản (.txt hoặc .csv)"])

    # Biến để lưu danh sách bình luận
    comments = []

    if option == "Nhập văn bản trực tiếp":
        # Nhập văn bản
        new_text = st.text_area("Nhập bình luận, mỗi bình luận trên một dòng:")

        st.markdown('Nội dung bình luận mẫu:')
        st.markdown('Đã mua đủ màu, rồi đổi sp khác nhưng vẫn phải quay lại với màu Hồng, dùng màu Hồng đi mn ơi, rất mềm mịn da, dùng 2-3 ngày thấy ngay khác biệt')
        # st.markdowm('BL2: 2 chai trước nghe mùi tràm trà giống nhau. Chai này mua bên Hasaki thấy mùi hôi kinh khủng khác mùi hoàn toàn so với chai trước dùng')

        if new_text.strip():
            comments = new_text.splitlines()

    elif option == "Tải file văn bản (.txt hoặc .csv)":
        uploaded_file = st.file_uploader("Tải file bình luận (.txt hoặc .csv):", type=['txt', 'csv'])
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.txt'):
                # Đọc file .txt
                content = uploaded_file.read().decode('utf-8')
                comments = content.splitlines()
            elif uploaded_file.name.endswith('.csv'):
                # Đọc file .csv
                df = pd.read_csv(uploaded_file)
                if 'comment' in df.columns:  # Kiểm tra cột dữ liệu
                    comments = df['comment'].dropna().tolist()
                else:
                    st.error("File CSV cần có cột tên 'comment' chứa nội dung bình luận!")
    
    if st.button("🎯 Dự đoán"):
        if comments:
            # Dự đoán xác suất và kết quả cho các bình luận
            results_with_prob = predict_new_data_with_probabilities(model, comments, vectorizer)

            # Hiển thị kết quả dưới dạng bảng
            st.subheader("🔍 Kết quả Dự đoán với Xác Suất và Kết Quả:")
            results_df = pd.DataFrame(results_with_prob)
            st.table(results_df)

            # Cho phép tải file kết quả về
            csv = results_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Tải kết quả dự đoán với xác suất về file CSV",
                data=csv,
                file_name="sentiment_predictions_with_results.csv",
                mime="text/csv"
            )
        else:
            st.warning("Vui lòng nhập bình luận hoặc tải file để dự đoán!")

            
except FileNotFoundError:
    st.error(f"Không tìm thấy file '{model_filename}' hoặc '{vectorizer_filename}'. Vui lòng kiểm tra lại đường dẫn file.")
except Exception as e:
    st.error(f"Đã xảy ra lỗi khi tải mô hình hoặc vectorizer: {e}")
