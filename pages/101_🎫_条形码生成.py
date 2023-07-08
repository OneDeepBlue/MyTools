import streamlit as st
import barcode
from barcode.writer import ImageWriter


BARCODE_MAP = ["code128", "ean8", "ean8-guard", "ean13", "ean13-guard", "ean", "gtin", "ean14", "jan", "upc", "upca",
               "isbn", "isbn13",
               "gs1", "isbn10", "issn", "code39", "pzn", "itf", "gs1_128", "codabar", "nw-7"]

barcode_map = st.selectbox("条码类型", BARCODE_MAP)

# 获取用户输入的条形码数据
barcode_str = st.text_area(label="🎫请输入条形码数据", height=200, max_chars=9999)
st.caption("支持批量操作，一行一个")
result = barcode_str.split("\n")  # 切割
barcode_list = [x for x in result if x]  # 去除空元素
expander = st.expander("更多设置")
background = expander.color_picker('背景颜色', '#f0f2f6')
foreground = expander.color_picker('条码颜色', '#000000')
write = [True, False]
write_text = expander.radio('显示文本', write, index=0, horizontal=True)
module_height = expander.slider('条码高度', 1, 30, value=8)
font_size = expander.slider('字号', 1, 20, value=6)
text_distance = expander.slider('条码字体间距', 1, 7, value=3)

if barcode_list:
    st.write("条码数量：", len(barcode_list))
    col1, col2 = st.columns(2)
    b_map = barcode.get_barcode_class(barcode_map)
    for i in range(len(barcode_list)):
        bar_code = b_map(barcode_list[i], writer=ImageWriter())
        bar_code.default_writer_options['module_height'] = module_height
        bar_code.default_writer_options['font_size'] = font_size
        bar_code.default_writer_options['text_distance'] = text_distance
        bar_code.default_writer_options['write_text'] = write_text
        bar_code.default_writer_options['background'] = background
        bar_code.default_writer_options['foreground'] = foreground
        # bar_code.default_writer_options['background'] = 'white'
        # bar_code.default_writer_options['module_width'] = module_width
        if i % 2:
            with col2:
                st.image(bar_code.render())
        else:
            with col1:
                st.image(bar_code.render())

