import pymysql
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta
import seaborn as sns
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.stats import norm
from tqdm import tqdm
from sklearn.metrics import mean_squared_error

con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'kyjin0413!',
                       db = 'lpointsample', charset = 'utf8')
cur = con.cursor(pymysql.cursors.DictCursor)
cur.execute(
    "select de_dt as 날짜 , sum(buy_am) as 금액 from 엘페이이용_view group by de_dt order by de_dt")
result=cur.fetchall()
con.commit()
con.close()
df= pd.DataFrame(result)

df.columns = ['date', 'price']
df = df.drop(['date'], axis = 1)

# strptime은 날짜와 시간 형식의 문자열을 datetime으로 변환해 줌
# strftime은 날짜와 시간(datetime)을 문자열로 출력
start = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")

# 기준 날짜에 대한 연산이 필요할 때 dateutil.relativedelta모듈의 relativedelta함수 이용
df_list = [start + relativedelta(days = x) for x in range(0, len(df)) ]

df['index'] = df_list

# set_index는 데이터프레임을 먼저 불러온 후, 특정 열을 인덱스로 설정할 때 사용
df.set_index( ['index'], inplace=True) 

# index 출력 X
df.index.name=None

df = df[:-31]

df = df.astype('int64')

# 그리드 서치(모델에게 가장 적합한 하이퍼 파라미터를 찾기) p, q

import itertools

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and d triplets
pdq = list( itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and d triplets
seasonal_pdq = [ (x[0], x[1], x[2], 334)  for x in pdq ]

print('Example of parameter combinations for Seasonal ARIMA ...')
print('SARIMAX:  {} x {}'.format(pdq[1], seasonal_pdq[1]) )
print('SARIMAX:  {} x {}'.format(pdq[1], seasonal_pdq[2]) )
print('SARIMAX:  {} x {}'.format(pdq[2], seasonal_pdq[3]) )
print('SARIMAX:  {} x {}'.format(pdq[2], seasonal_pdq[4]) )

# AIC(통계 모델을 성능을 측정하는 기준) - 낮을수록 좋음

select_candi = 10000000
param_candi = ( 0, 0, 0 )
param_seasonal_candi = ( 0, 0, 0)

count=0
end_count = len(pdq)

for param in pdq:   
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX( df['price'],
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False
                                           )
            results = mod.fit()
            count += 1
            if count <= 5:
                print('ARIMA{}x{}52 - AIC:{}'.format(param, param_seasonal, results.aic))
            
            if results.aic < select_candi:
                select_candi = results.aic
                param_candi = param
                param_seasonal_candi = param_seasonal
        except:
            continue
            
print(param_candi, param_seasonal_candi, select_candi) 

# 7: (1, 0, 1) (0, 1, 1, 7) 11584.586593938857
# 12: (1, 1, 1) (0, 1, 1, 12) 11342.920186033327
# 24: (1, 0, 1) (1, 1, 1, 24) 10461.834461076789
# 52: (1, 1, 1) (1, 1, 1, 52) 8410.510658969048
# 365: 오류
# 344: 

# mod = sm.tsa.statespace.SARIMAX(
#     df['price'],
#     order = (1, 1, 1),
#     seasonal_order = (1, 1, 1, 52),
#     # AR 매개 변수를 변환하여 모델의 자동 회귀 구성 요소에서 정상 성을 강제 적용할지 여부입니다. 기본값은 True입니다.
#     # AR항이 stationary를 만족하게끔 강제하는 것
#     enforce_stationarity = False,
#     # 모델의 이동 평균 구성 요소에서 반전 성을 강제하기 위해 MA 매개 변수를 변환할지 여부입니다. 기본값은 True입니다.
#     # MA항이 starionary를 만족하게끔 강제하는 것
#     enforce_invertibility = False
# )

# results = mod.fit()

# pred_uc = results.get_forecast( steps = 31 )
# forecast_mean = pred_uc.predicted_mean

#print(forecast_mean)

# actual = [77227183, 41526737, 69351467, 51247399, 68906456, 49715939, 35673851, 35659274, 48255147, 56768085, 69334618, 77053697, 57768387, 38486391, 31766615, 46015054, 51296762, 58203621, 54939758, 41869454, 51830618, 48838343 ,40257093, 44660225, 71313940, 67554989, 48002138, 38070210, 52093193, 47463341, 66341333]
# forecast7 = [49187920, 48980260, 73889980, 70159370, 68338800, 57508330, 48684330, 49368140, 49149540, 74048980, 70308710, 68479080, 57640090, 48808090, 49484380, 49258720, 74151530, 70405040, 68569550, 57725070, 48887910, 49559360, 49329140, 74217670, 70467160, 68627910, 57779880, 48939390, 49607710, 49374560, 74260330]
# forecast12 = [60194450, 59727190, 60096370, 63978410, 60916900, 60360360, 60625230, 57746520, 56553200, 58184600, 64327980, 66249350, 60497460, 61105150, 61715400, 65651500, 62602110, 62048290, 62313770, 59435190, 58241910, 59873310, 66016700, 67938060, 62186170, 62793860, 63404110, 67340210, 64290830, 63737010, 64002490]
# forecast24 = [42571810, 57402750, 70629990, 65991940, 69439780, 63662350, 61327470, 60797030, 60636350, 71057290, 69763530, 72313200, 59118510, 63139330, 65436690, 65491610, 57723400, 68472040, 72265290, 55796120, 48657390, 52679190, 64140600, 60506090, 62875560, 53516480, 64772240, 64953890, 68565660, 63316630, 60893780]
# forecast52 = [65326270, 62162170, 71835060, 60487780, 67213170, 59567890, 53090960, 57856400, 57113560, 72683900, 59299100, 58254290, 58019780, 62648590, 52459000, 59395100, 64560920, 62252610, 65689310, 47144950, 54909440, 51405470, 56998180, 56762280, 59813870, 58874300, 51486680, 51154790, 53979290, 67665560, 73416070]

# rmse = np.sqrt(mean_squared_error(actual, forecast12))

# print(rmse)