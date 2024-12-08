# import streamlit as st

# # Giả sử bạn có một danh sách sản phẩm
# products = [
#     "Sữa rửa mặt A",
#     "Sữa rửa mặt B",
#     "Dầu gội đầu C",
#     "Kem dưỡng da D",
#     "Sữa tắm E",
#     "Sữa rửa mặt chuyên sâu F"
# ]

# # Hàm tìm kiếm sản phẩm
# def search_products(query, products_list):
#     # Lọc danh sách sản phẩm dựa trên từ khóa tìm kiếm (có thể không phân biệt chữ hoa chữ thường)
#     results = [product for product in products_list if query.lower() in product.lower()]
#     return results

# # Kiểm tra nếu có sự thay đổi trong trạng thái nhập liệu
# if 'query' not in st.session_state:
#     st.session_state.query = ''

# # Tạo ô tìm kiếm cho người dùng
# query = st.text_input("Tìm kiếm sản phẩm", st.session_state.query)

# # Cập nhật query nếu có thay đổi
# if query != st.session_state.query:
#     st.session_state.query = query

# # Nếu người dùng nhập vào từ khóa, tìm các sản phẩm phù hợp
# if query:
#     results = search_products(query, products)
    
#     if results:
#         # Hiển thị kết quả tìm kiếm dưới ô nhập liệu
#         st.write("Danh sách sản phẩm đề xuất:")
#         for product in results:
#             st.write(f"- {product}")  # Hiển thị sản phẩm phù hợp
#     else:
#         st.write("Không có sản phẩm nào phù hợp với từ khóa tìm kiếm của bạn.")
# else:
#     st.write("Nhập từ khóa để tìm kiếm sản phẩm.")

#_____________________________________

# import streamlit as st
# import pandas as pd

# # Giả sử bạn có DataFrame chứa thông tin sản phẩm
# data = {
#     'id_product': [1, 2, 3, 4, 5],
#     'ten_san_pham': ['Sữa rửa mặt A', 'Sữa rửa mặt B', 'Dầu gội đầu C', 'Kem dưỡng da D', 'Sữa tắm E']
# }
# df_products = pd.DataFrame(data)

# # Tạo selectbox cho người dùng chọn sản phẩm từ tên sản phẩm
# selected_product_name = st.selectbox("Chọn sản phẩm", df_products['ten_san_pham'])

# # Tìm id của sản phẩm đã chọn
# selected_product_id = df_products[df_products['ten_san_pham'] == selected_product_name]['id_product'].values[0]

# # Hiển thị thông tin sản phẩm đã chọn
# st.write(f"Sản phẩm bạn đã chọn: {selected_product_name} (ID: {selected_product_id})")

# import streamlit as st
# import requests
# from bs4 import BeautifulSoup

# # Hàm lấy thông tin sản phẩm từ link
# def get_product_info(url):
#     # Gửi yêu cầu GET đến trang web
#     response = requests.get(url)
    
#     # Kiểm tra xem trang web có phản hồi thành công không
#     if response.status_code == 200:
#         # Phân tích HTML của trang web bằng BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Lấy hình ảnh sản phẩm (sử dụng thẻ img và các thuộc tính phù hợp)
#         img_tag = soup.find('img', {'class': 'product-image'})  # Lọc thẻ img có class phù hợp
#         img_url = img_tag['src'] if img_tag else None
        
#         # Lấy các thông tin khác của sản phẩm (ví dụ: tên, giá, mô tả)
#         name_tag = soup.find('h1', {'class': 'product-name'})  # Lọc tên sản phẩm
#         product_name = name_tag.text.strip() if name_tag else 'Tên sản phẩm không tìm thấy'
        
#         price_tag = soup.find('span', {'class': 'price'})  # Lọc giá sản phẩm
#         price = price_tag.text.strip() if price_tag else 'Giá không tìm thấy'
        
#         return img_url, product_name, price
#     else:
#         st.error("Không thể tải trang sản phẩm.")
#         return None, None, None

# # Tạo ô nhập link và gọi hàm lấy thông tin
# link = st.text_input("Nhập link sản phẩm:")

# if link:
#     img_url, product_name, price = get_product_info(link)

#     if img_url:
#         # Hiển thị thông tin sản phẩm trong một ô vuông
#         with st.expander("Thông tin sản phẩm"):
#             st.write(f"**Tên sản phẩm**: {product_name}")
#             st.write(f"**Giá**: {price}")
#             st.image(img_url, caption=product_name, use_column_width=True)
#             st.markdown(f"[Xem sản phẩm tại đây]({link})")


