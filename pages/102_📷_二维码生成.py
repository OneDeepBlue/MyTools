import qrcode
import streamlit as st

st.set_page_config(page_title="二维码生成", page_icon="📷", layout="centered",
                   initial_sidebar_state="expanded")

# 获取用户输入的条形码数据
qrcode_str = st.text_area(label="🎫请输入条形码数据", height=200, key="qrcode", max_chars=9999)
st.caption("支持批量操作，一行一个")
result = qrcode_str.split("\n")  # 切割
qrcode_list = [x for x in result if x]  # 去除空元素
# 生成二维码对象
# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# # 添加数据到二维码对象中
# qr.add_data(data)
# # 建立二维码矩阵
# qr.make(fit=True)
# # 生成二维码图片
# img = qr.make_image(fill_color="black", back_color="white")

if qrcode_list:
    st.write("条码数量：", len(qrcode_list))
    qrcode_col1, qrcode_col2 = st.columns(2)
    for i in range(len(qrcode_list)):
        img = qrcode.make(qrcode_list[i])
        if i % 2:
            with qrcode_col2:
                st.image(img.get_image())
                st.caption(qrcode_list[i])
        else:
            with qrcode_col1:
                st.image(img.get_image())
                st.caption(qrcode_list[i])
