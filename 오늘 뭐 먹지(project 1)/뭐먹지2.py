from random import *
import pandas as pd

# 음식 데이터 - 파일
fooddata = pd.read_excel('..\\아이디어박스\\FoodData2.xlsx')

# 데이터 컬럼 (음식이름, 음식종류, 맵기)
fooddatacol = fooddata.columns

# 모든 데이터
Food = fooddata['음식이름']
Type = fooddata['음식종류']
Hot = fooddata['맵기']

# 나라별: Type2
Type2 = fooddata.drop_duplicates(['음식종류'])
Type2 = Type2['음식종류'].values

print(f"골라주세요 => {Type2}")

print()

food = input("오늘 끌리는 음식 종류는? => ")

print()

# 맵기 정도: Type3
Type3 = fooddata.drop_duplicates(['맵기'])
Type3 = Type3['맵기'].values
Type3

print(f"골라주세요 => {Type3}")

print()

spicy = input("매운 정도는? => ")

# 한식 & 순한 맛
KH1 = fooddata.loc[(fooddata['맵기'] == '순한 맛') & (fooddata['음식종류'] == "한식")]
KH1 = KH1['음식이름'].values
KH1 = choice(KH1)

# 한식 & 보통 맛
KH2 = fooddata.loc[(fooddata['맵기'] == '보통 맛') & (fooddata['음식종류'] == "한식")]
KH2 = KH2['음식이름'].values
KH2 = choice(KH2)

# 한식 & 매운 맛
KH3 = fooddata.loc[(fooddata['맵기'] == '매운 맛') & (fooddata['음식종류'] == "한식")]
KH3 = KH3['음식이름'].values
KH3 = choice(KH3)

# 한식 & 맵기 조절 가능
KH4 = fooddata.loc[(fooddata['맵기'] == '맵기 조절 가능') & (fooddata['음식종류'] == "한식")]
KH4 = KH4['음식이름'].values
KH4 = choice(KH4)

if (food == "한식"):
    if (spicy == "순한 맛"):
        print(f'{KH1} 는/은 어때요?')
    elif (spicy == "보통 맛"):
        print(f'{KH2} 는/은 어때요?')
    elif (spicy == "매운 맛"):
        print(f'{KH3} 는/은 어때요?')
    elif (spicy == "맵기 조절 가능"):
        print(f'{KH4} 는/은 어때요?')
    else:
        print("잠시만 기다려주세요.")