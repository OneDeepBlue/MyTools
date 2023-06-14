import json
from jsonpath_rw_ext import parse

import streamlit as st

st.set_page_config(page_title="JSON格式化", page_icon=":100:", layout="centered",
                   initial_sidebar_state="expanded")

json_str = st.text_area(label="请输入json数据", height=200)
if json_str:
    json_obj = json.loads(json_str)
    expander = st.expander("JSON提取")
    jsonPath = expander.text_input('jsonPath表达式', value='', max_chars=None)
    button = expander.button("执行")
    if button:
        if not jsonPath:
            expander.error("jsonPath不能为空")
        else:
            try:
                expr = parse(jsonPath)
                data_list = [match.value for match in expr.find(json_obj)]
                expander.write(data_list)
            except:
                expander.error("jsonPath表达式有误，请检查后重试")
    st.write("已生成，可选择复制👇")
    st.write(json_obj)
