import pandas as pd

UserDf=pd.read_csv(r'.\UserList.csv')# data에 읽은 값 저장

# 도서 검색
def Search(InStandard,InSearch): 
    
    if InStandard=="회원 명":                  # 회원 명 선택 시
        SearchIndex="USER_NAME"               # 회원 데이터 다루기
    elif InStandard=="전화번호":                # 전화번호 선택 시
        SearchIndex="USER_PHONE"              # 회원 데이터 다루기

    if UserDf[SearchIndex].str.contains(InSearch).any():
        return UserDf.loc[UserDf[SearchIndex].str.contains(InSearch)]
    elif InSearch == '':
        return UserDf