import random

import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="时间计算器", page_icon="⏱", layout="centered",
                   initial_sidebar_state="expanded")

def is_workday(date):
    # 判断是否为周六周日
    if date.weekday() >= 5:
        return False
    # 其余情况均为工作日
    return True


def add_workdays(start_date, days):
    if days == 0:
        return start_date
    delta = timedelta(days=1 if days > 0 else -1)
    end_date = start_date
    count = 0
    while count < abs(days):
        end_date += delta
        if is_workday(end_date):
            count += 1
    return end_date


tab1, tab2, tab3, tab4 = st.tabs(["计算两时间差", "计算结束时间", "时间戳转时间", "时间转时间戳"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        date = datetime.now() - timedelta(days=15)
        date_i = st.date_input("起始日期", value=date)
        date_e = st.date_input("结束日期")
    with col2:
        time_i = st.time_input("时间", step=60, key="time_i")
        time_e = st.time_input("时间", step=60, key="time_e")
    # 定义要计算的日期
    date_str = f"{date_i} {time_i}"
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    # now_date = datetime.now()
    date_str = f"{date_e} {time_e}"
    now_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    # 计算与当前日期的时间差
    diff = now_date - date
    st.success(f"相差：{diff.days}天 {diff.seconds // 3600}小时 {(diff.seconds // 60) % 60}分钟")

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        date_s = st.date_input("日期", key="date_s")
    with col2:
        days = st.number_input("天数", step=0, min_value=-36500, value=0)
    with col3:
        st.write("")
        st.write("")
        weekday = st.checkbox('工作日', value=False)
    if weekday:
        end_date_str = add_workdays(date_s, days)
    else:
        end_date = date_s + timedelta(days=days)
        end_date_str = end_date.strftime("%Y-%m-%d")
    st.success(f"结果：{end_date_str}")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        timestamp = st.number_input("时间戳", step=0)
    with col2:
        time_items = ["秒（10位）", "毫秒（13位）"]
        time_unit = st.radio('单位', time_items, index=0, horizontal=True)
    if timestamp:
        if time_unit == "毫秒（13位）":
            timestamp = timestamp / 1000
        # 将时间戳转换为datetime对象
        dt_object = datetime.fromtimestamp(timestamp)
        # 将datetime对象格式化为字符串
        date_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        st.success(f"转换后：{date_string}")

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        date_d = st.date_input("日期", key="date_d")
    with col2:
        time_d = st.time_input("时间", step=60)
    date_string = f"{date_d} {time_d}"
    # 将日期时间字符串转换为datetime对象
    dt_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    # 将datetime对象转换为时间戳
    timestamp = dt_object.timestamp()
    st.success(f"10位：{int(timestamp)}")
    st.success(f"13位：{int(timestamp)}{random.randint(111, 999)}")
