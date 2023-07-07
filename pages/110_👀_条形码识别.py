# import cv2
# import streamlit as st
# from pyzbar import pyzbar
# import numpy as np

# st.set_page_config(page_title="识别条码", page_icon="👀", layout="centered",
#                    initial_sidebar_state="expanded")


# def decode_barcode(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     barcodes = pyzbar.decode(gray)

#     for barcode in barcodes:
#         x, y, w, h = barcode.rect
#         barcode_info = barcode.data.decode('utf-8')

#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(image, barcode_info, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#         st.success(f"条形码信息：{barcode_info}", )

#     return image


# st.title("条形码识别")
# uploaded_file = st.file_uploader("上传图像文件", type=['jpg', 'jpeg', 'png'])

# if uploaded_file is not None:
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

#     # st.image(image, channels="BGR", caption="上传的图像")

#     image_with_barcode = decode_barcode(image)

#     st.image(image_with_barcode, channels="BGR", caption="识别结果")
