import time

import streamlit as st
import pandas as pd


sidebar_obj = st.sidebar
# 创建侧边栏菜单
sidebar_obj.header("功能")
menu_items = ["主页", "入库", "出库", "🚜叉车任务执行"]
selected_item = sidebar_obj.radio('请选择菜单项👇', menu_items, index=0)
# selected_item = sidebar_obj.selectbox("请选择菜单项", menu_items)

env_items = ["开发环境", "测试环境", "线上环境"]
env = sidebar_obj.selectbox("请选择运行环境", env_items)


button2 = st.button("看看气球")
button3 = st.button("雪花")
if button2:
    st.balloons()  # 气球效果
    # st.snow()  # 雪花效果
    with st.spinner('执行中。。。'):
        time.sleep(2)
    st.success('Done!')
    progress_text = "执行中，请稍等。。"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
if button3:
    st.snow()
st.title("这是标题")
st.warning("警告")
st.checkbox('复选框1', value=False)
st.checkbox('复选框2', value=False)
st.radio('单选框', menu_items, index=0)
st.selectbox('下拉框', menu_items, index=0)
st.multiselect('多选框', menu_items, default=None)
st.slider('滑块', 10, 100, value=None, step=None)
st.text_input('文本输入框', value='', max_chars=None)
st.number_input('数字输入框', min_value=None, max_value=None, value=1, step=None)
st.text_area('多行文本输入框', value='', max_chars=None)
st.date_input('日期输入框', value=None, min_value=None, max_value=None)
st.time_input('时间输入框', value=None)
st.file_uploader('文件上传', type=None, accept_multiple_files=False)
options = ['新增', '已审核', '待备货', '备货中', '待复核', '复核中', '复核完成', '出库完成']
color = st.select_slider('Select a color of the rainbow', options=options)

data = [{"allCount": 281, "queryDate": "05-02"}, {"allCount": 211, "queryDate": "05-03"},
        {"allCount": 200, "queryDate": "05-04"}, {"allCount": 233, "queryDate": "05-05"},
        {"allCount": 241, "queryDate": "05-06"}, {"allCount": 225, "queryDate": "05-07"},
        {"allCount": 190, "queryDate": "05-08"}, {"allCount": 204, "queryDate": "05-09"},
        {"allCount": 193, "queryDate": "05-10"}, {"allCount": 510, "queryDate": "05-11"},
        {"allCount": 434, "queryDate": "05-12"}, {"allCount": 201, "queryDate": "05-13"},
        {"allCount": 269, "queryDate": "05-14"}]
# 转换数据格式
dates = [item["queryDate"] for item in data]
counts = [item["allCount"] for item in data]
sales = pd.Series(counts, index=dates, name="销量")
# 绘制柱形图
st.write("柱形图")
st.bar_chart(sales)
st.write("面积图")
st.area_chart(sales)
st.write("折线图")
st.line_chart(sales)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

name = st.text_input('Name')
if not name:
    st.warning('Please input a name.')
    st.stop()
st.success('Thank you for inputting a name.')
