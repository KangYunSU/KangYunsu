from random import *
import pandas as pd

# # 음식 데이터 - 리스트 (리스트로 안해도 됨)
# food_type = ['한식', '양식', '중식', '일식', '아시아']

# Korean = '국밥', '떡볶이', '불고기', '비빔밥', '김밥'
# Western = ['피자', '파스타', '스테이크', '샐러드', '리조또']
# Chinese = ['자장면', '마라탕', '훠궈', '양꼬치', '마파두부']
# Japanese = ['초밥', '우동', '메밀소바', '돈가스', '훗토마끼']
# Asian = ['쌀국수', '나시고랭', '카레', '똠양꿍', '팟타이']

# K = choice(Korean)
# W = choice(Western)
# C = choice(Chinese)
# J = choice(Japanese)
# A = choice(Asian)

#################################################################

# 음식 데이터 - 파일
fooddata = pd.read_excel('아이디어박스\\FoodData1.xlsx')

food_type = fooddata.columns

# 나라별 음식 예시
Korean = fooddata['한식']
Western = fooddata['양식']
Chinese = fooddata['중식']
Japanese = fooddata['일식']
Asian = fooddata['아시안']
Pop = fooddata['인기']

# 랜덤으로 나라별 음식 하나 골라줌
K = choice(Korean)
W = choice(Western)
C = choice(Chinese)
J = choice(Japanese)
A = choice(Asian)
P = choice(Pop)

print(f"골라보세요 => {food_type}")

print()

food = input("오늘 끌리는 건? => ")

if (food == '한식'):
    print(f'{K} 는/은 어때요?')

if (food == '양식'):
    print(f'{W} 는/은 어때요?')

if (food == '중식'):
    print(f'{C} 는/은 어때요?')

if (food == '일식'):
    print(f'{J} 는/은 어때요?')

if (food == '아시아'):
    print(f'{A} 는/은 어때요?')

if (food == '인기'):
    print(f'{P} 는/은 어때요?')

else:
    print('준비 중이니 기다려주세요!')