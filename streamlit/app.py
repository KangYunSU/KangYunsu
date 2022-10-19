import streamlit as st
import pandas as pd
from random import *

# 페이지 기본 설정
st.set_page_config(
    page_icon = "🍽️",
    page_title = "오늘 뭐 먹지?",
    layout = 'wide')

# 파일 - 데이터 프레임 
fooddata = pd.read_csv('FoodData2.csv')
fooddata = pd.DataFrame(fooddata)

# 이미지 첨부 - 웹 배너
st.image('picture1.png', use_column_width = True)

# 페이지 헤더, 서브헤더 제목 설정

test_title = """
<h2 style = "color: rgb(255, 165, 0); font-weight: bold; font-size : 35px; text-align : center;">👑 오늘의 인기 메뉴 👑</h2>
<h2 style = "color:black; font-weight: light; font-size : 30px; text-align : center;">1위 마라탕</h2>
<h2 style = "color:black; font-weight: light; font-size : 30px; text-align : center;">2위 로제떡볶이</h2>
"""
st.markdown(test_title, unsafe_allow_html = True)
st.markdown('---')

# 나라별: Type1
Type1 = fooddata.drop_duplicates(['음식종류'])
Type1 = Type1['음식종류'].values

# 맵기 정도: Type2
Type2 = fooddata.drop_duplicates(['맵기'])
Type2 = Type2['맵기'].values

# 메뉴 추천 버튼
option1 = st.selectbox(
    '오늘 땡기는 건?',
    (Type1))

option2 = st.selectbox(
    '맵기는?',
    (Type2))

# 추천 코드
@st.cache
def type_choice(food1, spicy1):

    fs = ''

    fstype = fooddata.loc[(fooddata['맵기'] == spicy1) & (fooddata['음식종류'] == food1)]
    fstype = fstype['음식이름'].values

    if fs not in fstype:
        fs += fstype
        
    if fs in fstype:
        fstype = choice(fstype)
        return fstype

    else: 
        no = "준비 중입니다"
        return no

result = type_choice(option1, option2)

st.write("")
st.metric('오늘의 추천 음식은 😋', result)

# 꾸미기 - metric
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: white;
   border: 1px solid black;
   padding: 3% 3% 3% 3%;
   border-radius: 5px;
   color: black;
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: green;
}
</style>
"""
, unsafe_allow_html = True)