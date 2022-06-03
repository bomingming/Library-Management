import pandas as pd
from datetime import datetime

f=open('BookList.csv','r',encoding='utf-8')
BookDf=pd.read_csv(r'.\BookList.csv')# data에 읽은 값 저장
# header=next(data) #csv파일의 1행 제거

# 도서 검색
def Search(InStandard,InSearch): 
    if InStandard=="도서 명":                  # 도서 명 선택 시
        SearchIndex="BOOK_TITLE"               # 도서 데이터 다루기
    elif InStandard=="저자":                   # 저자 선택 시
        SearchIndex="BOOK_AUTHOR"              # 저자 데이터 다루기
    elif InStandard=="출판사":                 # 출판사 선택 시
        SearchIndex="BOOK_PUB"                 # 출판사 데이터 다루기

    if BookDf[SearchIndex].str.contains(InSearch).any():
        return(BookDf.loc[BookDf[SearchIndex].str.contains(InSearch)])
            #수정한 정보를 데이터 프레임에 추가