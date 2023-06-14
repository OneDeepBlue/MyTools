import streamlit as st

from common import mock

st.set_page_config(page_title="数据生成", page_icon=":100:", layout="centered",
                   initial_sidebar_state="expanded")

data_type = ["身份证号", "手机号", "姓名", "车牌号"]

_type = st.selectbox("数据类型", data_type)
number = st.number_input("数量", value=10, step=10)
button = st.button("🎲 生成")
data = ""

if button:
    if _type == "身份证号":
        for i in range(number):
            data += str(mock.mock_id()) + "\n"
    elif _type == "手机号":
        for i in range(number):
            data += str(mock.mock_phone()) + "\n"
    elif _type == "姓名":
        for i in range(number):
            data += str(mock.mock_cname()) + "\n"
    elif _type == "车牌号":
        for i in range(number):
            data += str(mock.mock_carno()) + "\n"
    st.write(f"已生成{_type}数量：", number)
    st.code(data, line_numbers=True)

