import io
import os
import random
import streamlit as st
from xmindparser import xmind_to_dict
from openpyxl import Workbook
from openpyxl.styles import Font
import tempfile
import pandas as pd


# 递归遍历主题树，获取父主题和最小子主题的内容
def traverse_topics(topic, parent_titles, result):
    parent_titles.append(topic["title"])
    # 如果当前主题没有子主题，则将父主题和最小子主题的内容添加到结果列表中
    if "topics" not in topic:
        result.append(("/".join(parent_titles[:-1]), topic["title"]))
    # 如果当前主题有子主题，则递归遍历子主题
    else:
        for sub_topic in topic["topics"]:
            traverse_topics(sub_topic, parent_titles, result)

    # 递归完成后，移除当前主题的标题，返回上一级主题
    parent_titles.pop()


# 创建Streamlit应用程序
st.title("Xmind转Excel")
# 创建文件上传部件
file = st.file_uploader("上传Xmind文件", type=".xmind")
# 当用户上传文件时
if file is not None:
    # 保存Xmind文件为临时文件
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(file.read())
    temp_file.close()

    # 读取 Xmind 文件并解析为字典
    xmind_dict = xmind_to_dict(temp_file.name)
    # 获取根主题
    root_topic = xmind_dict[0]["topic"]
    # 存储结果的列表
    result_list = []
    # 递归遍历主题树，得到父主题和最小子主题的内容
    traverse_topics(root_topic, [], result_list)
    # 创建一个新的 Excel 文件
    workbook = Workbook()
    sheet = workbook.active
    # 创建一个Font对象，并设置加粗
    bold_font = Font(bold=True)
    # 将加粗样式应用于各单元格
    sheet['A1'].font = bold_font
    sheet['B1'].font = bold_font
    sheet['C1'].font = bold_font
    sheet['D1'].font = bold_font
    sheet['E1'].font = bold_font
    sheet['F1'].font = bold_font
    sheet['G1'].font = bold_font
    sheet['H1'].font = bold_font
    sheet['I1'].font = bold_font
    # 写入标题
    sheet['A1'] = '用例编号'
    sheet['B1'] = '项目模块'
    sheet['C1'] = '用例标题'
    sheet['D1'] = '优先级'
    sheet['E1'] = '预置条件'
    sheet['F1'] = '测试输入'
    sheet['G1'] = '操作步骤'
    sheet['H1'] = '预期结果'
    sheet['I1'] = '用例状态'

    values = ["高", "中", "低"]  # 数值
    weights = [40, 50, 10]  # 概率

    # 写入数据
    for index, item in enumerate(result_list, start=2):
        result = random.choices(values, weights)[0]
        parent_title, child_title = item
        sheet[f'A{index}'] = index - 1
        sheet[f'B{index}'] = parent_title
        sheet[f'C{index}'] = "".join(char for char in child_title if char not in "【预期】")
        sheet[f'D{index}'] = result
        sheet[f'E{index}'] = "/"
        sheet[f'F{index}'] = "/"
        sheet[f'G{index}'] = "/"
        sheet[f'H{index}'] = child_title
        sheet[f'I{index}'] = "通过"
    # 保存Excel文件
    excel_file = io.BytesIO()
    workbook.save(excel_file)
    excel_file.seek(0)

    # 删除临时文件
    os.remove(temp_file.name)

    # 提供下载链接给用户
    st.write("点击下载Excel文件")
    st.download_button("下载", excel_file, file_name="xmind_to_excel.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    # 读取Excel文件并展示在界面上
    df = pd.read_excel(excel_file)
    st.write("预览")
    st.dataframe(df)

