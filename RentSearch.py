#from tkinter.tix import COLUMN
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
    '''
    COL=BookDf['BOOK_RENT']
    
    for i in COL[0:]:
        COL!=False'''

    PrintB=BookDf.loc[BookDf[SearchIndex].str.contains(InSearch)]
    PrintB=PrintB.loc[BookDf['BOOK_RENT'].str.contains("대여 중")]
    return PrintB


'''
    b=BookDf.keys()
    ReturnRentBook=pd.DataFrame(columns=b)
    
    a=BookDf.loc[BookDf[SearchIndex].str.contains(InSearch)]
    for i in a.index:
        if a.loc[i,'BOOK_RENT']==False:
            ReturnRentBook=pd.concat(ReturnRentBook,a.loc[i])
    return ReturnRentBook
    

#'반납'메뉴 선택 후 검색 창의 결과 값과 csv파일의 rent되어 있는 결과 비교 
    #index값을 기준으로 비교
    for i in BookDf.index:
        #rent된df를 저장해 놓을 df
        if BookDf.loc[i,'BOOK_RENT']=="TRUE":
                RentDf=BookDf.loc[i]
        #내가 입력한 값이 목록에 있는경우
        if BookDf.loc[SearchIndex].str.contains(InSearch):
            #목록에 있는 책이 rent된 경우
            if BookDf.loc[i,'BOOK_RENT']=="TRUE":
                return BookDf.loc[i]
            #책이 rent가 안된 경우
            else:
                print("이미 반납이 완료된 도서입니다.")
        #내가 아무것도 입력하지 않고 엔터를 누른 경우
        elif InSearch == '':
            return RentDf
        #내가 입력한 값이 목록에 없는 경우
        else:
            print("목록에 없는 책입니다.")'''