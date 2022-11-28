import csv
import os

import pandas as pd

# 엑셀 파일 추출
file_df = pd.read_excel('파일 이름을 입력하세요.xls')

# csv 파일에서 특정 열 추출
name = file_df.loc[:, '이름']
phone = file_df.loc[:, '휴대폰']

name_list = list(name)
phone_list = list(phone)

# 이름과 휴대폰 번호 정제후 리스트 타입 만들기
last = []
first = []
phone = []
for i,j in zip(name_list, phone_list):
    # 성과 이름 분리하기
    last.append(i[:1])
    first.append(i[1:3])
    # 휴대폰 번호가 공백일 경우는 공백으로 그대로 삽입
    if isinstance(j, str) == True:
        ph = str(j)
        new_ph = ph.replace('-', '')
    else:
        new_ph = ''
    phone.append(new_ph)

# 원본 데이터 데이터프레임 생성 후 csv 파일 만들기
# to_csv : index 는 false 여야 번호 생성을 안한다.
all_col = file_df.iloc[:, 2:14].copy()
all_df = pd.DataFrame.from_dict(all_col)
all_c = all_df.to_csv('main.csv', encoding='utf-8-sig',index=False)

# csv 파일에 특정 열 삽입
# csv 파일을 데이터프레임으로 변환한다.
# 성, 이름, 휴대폰 번호는 리스트 타입으로 삽입
df = pd.read_csv('main.csv')
df.insert(0, '출입처구분', '')
df.insert(0, '기자등급', '')
df.insert(0, '성별', '')
df.insert(0, '휴대폰', phone)
df.insert(0, '이름', first)
df.insert(0, '성', last)

# 다시 데이터프레임을 csv파일로 변환한다.
df.to_csv('result.csv', encoding='utf-8-sig',index=False)



