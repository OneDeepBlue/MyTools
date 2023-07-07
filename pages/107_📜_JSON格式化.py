import json
import re

from jsonpath_rw_ext import parse

import streamlit as st

st.set_page_config(page_title="JSON格式化", page_icon="📜", layout="centered",
                   initial_sidebar_state="expanded")

json_str = st.text_area(label="请输入json数据", height=200)
if json_str:
    try:
        json_obj = json.loads(json_str)
    except json.JSONDecodeError as e:
        # 从错误信息中提取出错误位置信息
        match = re.search(r"line (\d+) column (\d+)", str(e))
        if match:
            line = int(match.group(1))
            column = int(match.group(2))
            st.error(f"😟 JSON格式错误，第 {line} 行第 {column} 列出现了错误!")
            st.stop()
        else:
            st.error("😟 JSON格式错误，无法解析!")
            st.stop()
    expander = st.expander("JSON提取")
    jsonPath = expander.text_input('jsonPath表达式', value='', max_chars=None)
    button = expander.button("执行")
    if button:
        if not jsonPath:
            expander.error("😟 jsonPath不能为空")
        else:
            try:
                expr = parse(jsonPath)
                data_list = [match.value for match in expr.find(json_obj)]
                expander.write(data_list)
            except:
                expander.error("😟 jsonPath表达式有误，请检查后重试")
    st.write("已生成，可选择复制👇")
    st.write(json_obj)
