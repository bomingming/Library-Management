from traceback import print_tb
import pandas as pd

BookDf=pd.read_csv('BookList.csv')# data에 읽은 값 저장

# 도서 검색
def Search(InStandard,InSearch):        #INSEARCH - 내가 검색창에 입력한 값이 저장되어 있음
    if InStandard=="도서 명":                  # 도서 명 선택 시
        SearchIndex="BOOK_TITLE"               # 도서 데이터 다루기
    elif InStandard=="저자":                   # 저자 선택 시
        SearchIndex="BOOK_AUTHOR"              # 저자 데이터 다루기
    elif InStandard=="출판사":                 # 출판사 선택 시
        SearchIndex="BOOK_PUB"                 # 출판사 데이터 다루기

    PrintB=BookDf.loc[BookDf[SearchIndex].str.contains(InSearch)]
    PrintB=PrintB.loc[BookDf['BOOK_RENT'].str.contains("대여 중")]
    return PrintB