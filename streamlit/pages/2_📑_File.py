import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_icon = "🥄",
    page_title = "오늘 뭐 먹지?",
    layout = 'wide'
)

fooddata = pd.read_csv('FoodData2.csv')
fooddata = pd.DataFrame(fooddata)

# 제목
st.header('필요한 파일 / 이미지')

# 파일 다운로드 버튼
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(fooddata)

st.download_button(
    label="fooddata 다운로드",
    data=csv,
    file_name='FoodData.csv',
    mime='text/csv',
)

# 이미지 다운로트 버튼
with open("picture1.png", "rb") as file:
    btn = st.download_button(
            label="오늘 뭐 먹지? 이미지 다운로드",
            data=file,
            file_name="picture.png",
            mime="image/png"
          )