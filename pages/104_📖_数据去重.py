import streamlit as st

from collections import OrderedDict

data_str = st.text_area(label="📄原数据", height=200)
a = ""
b = ""
if data_str:
    result = [x for x in data_str.split("\n") if x]  # 去除空元素
    s = list(OrderedDict.fromkeys(result))  # 去重并保持顺序
    repeated = []
    for i in s:
        if result.count(i) > 1:
            repeated.append(i)
    a = "\n".join(s)  # 将列表转换为字符串
    b = "\n".join(repeated)  # 将列表转换为字符串
    st.caption(f"原总行数：{len(result)}")
    st.caption(f"去重后总行数：{len(s)}")
col1, col2 = st.columns(2)
with col1:
    st.write("去重后的内容(不包含空行)👇")
    st.code(a, line_numbers=True)
with col2:
    st.write("重复的内容👇")
    st.code(b, line_numbers=True)