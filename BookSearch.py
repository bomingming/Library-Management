import pandas as pd

f=open('BookList.csv','r',encoding='utf-8')
BookDf=pd.read_csv(r'.\BookList.csv')# data에 읽은 값 저장

# 도서 검색
def Search(InStandard,InSearch): 
    if InStandard=="도서 명":                  # 도서 명 선택 시
        SearchIndex="BOOK_TITLE"               # 도서 데이터 다루기
    elif InStandard=="저자":                   # 저자 선택 시
        SearchIndex="BOOK_AUTHOR"              # 저자 데이터 다루기
    elif InStandard=="출판사":                 # 출판사 선택 시
        SearchIndex="BOOK_PUB"                 # 출판사 데이터 다루기

    if BookDf[SearchIndex].str.contains(InSearch).any():
        return BookDf.loc[BookDf[SearchIndex].str.contains(InSearch)]
    elif InSearch == '':
        return BookDf
    else:
        return "결과값 없음"