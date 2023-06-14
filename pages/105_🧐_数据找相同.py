import streamlit as st

st.write("判断两个数据中是否存在相同的数据行，并显示出来")

col1, col2 = st.columns(2)

with col1:
    data_str = st.text_area(label="📝原数据", height=400)
    result = [x for x in data_str.split("\n") if x]  # 去除空元素
    st.write(len(result))

with col2:
    data_str2 = st.text_area(label="📑对比数据", height=400)
    result2 = [x for x in data_str2.split("\n") if x]  # 去除空元素
    st.write(len(result2))

# 使用set函数将列表a和b转换为集合类型，并使用&操作符获得两个集合的交集，最后将交集再转换回列表类型并赋值给变量c
# c = list(set(result) & set(result2))
with st.spinner('数据较多，请稍等...'):
    c = [i for j, i in enumerate(result) if i in result2 and i not in result[:j]]  # 另一种方法，这个输出的元素顺序不变
d = "\n".join(c)

st.write("")
st.write("相同的数据(不包含空行)👇")
st.code(d, line_numbers=True)
st.write("共", len(c), "行")
