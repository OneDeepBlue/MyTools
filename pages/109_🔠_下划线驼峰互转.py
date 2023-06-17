import re

import streamlit as st

data_str = st.text_area(value="hump_example\nhump_example_more", label="📝待转换内容", height=200)
col1, col2 = st.columns(2)
with col1:
    but = st.button("下划线转驼峰")
with col2:
    but2 = st.button("驼峰转下划线")

str_list = [x for x in data_str.split("\n") if x]  # 转换成list并去除空元素
repeated = []

if but:
    for i in str_list:
        # 将字符串按下划线分割成单词列表，将除首单词外的其他单词首字母大写，再将单词列表拼接成一个字符串
        s = ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(i.split('_')))
        repeated.append(s)

if but2:
    for i in str_list:
        # 使用正则表达式匹配所有大写字母前的字符，并在其后面加上下划线，再将字符串全部转为小写
        s = re.sub(r'([a-z]+)([A-Z])', r'\1_\2', i).lower()
        repeated.append(s)

result = "\n".join(repeated)
st.write("转换结果👇")
st.code(result, line_numbers=True)