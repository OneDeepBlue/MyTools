import qrcode
import streamlit as st


# 获取用户输入的条形码数据
barcode_str = st.text_area(label="🎫请输入条形码数据", height=200)
st.caption("支持批量操作，一行一个，理论上无限制条数 :sunglasses:")
result = barcode_str.split("\n")  # 切割
barcode_list = [x for x in result if x]  # 去除空元素
# 生成二维码对象
# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# # 添加数据到二维码对象中
# qr.add_data(data)
# # 建立二维码矩阵
# qr.make(fit=True)
# # 生成二维码图片
# img = qr.make_image(fill_color="black", back_color="white")

if barcode_list:
    st.write("条码数量：", len(barcode_list))
    col1, col2 = st.columns(2)
    for i in range(len(barcode_list)):
        img = qrcode.make(barcode_list[i])
        if i % 2:
            with col2:
                st.image(img.get_image())
                st.caption(barcode_list[i])
        else:
            with col1:
                st.image(img.get_image())
                st.caption(barcode_list[i])
