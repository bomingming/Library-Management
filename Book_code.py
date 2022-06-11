import pandas as pd
import csv
from datetime import datetime
#from Rent_code import RentDf as RDf


BookField=['BOOK_TITLE','BOOK_ISBN', 'BOOK_AUTHOR', 'BOOK_PUB','BOOK_PRICE', 'BOOK_LINK', 'BOOK_INFOR', 'BOOK_RENT', 'BOOK_PIC']    #필드 명 리스트

BookDf=pd.DataFrame({'BOOK_TITLE':['데미안','삼국유사','수레바퀴 아래서','언제나 밤인 세계'],
         'BOOK_ISBN':['9788937460449','9788937461668','9788937460500','9791170520634'],
         'BOOK_AUTHOR':['헤르만 헤세','일연','헤르만 헤세','하지은'],
         'BOOK_PUB':['민음사','민음사','민음사','황금가지'],
         'BOOK_PRICE':['8000','15000','8000','16800'],
         'BOOK_LINK':['https://A', 'https://B', 'https://C', 'https://D'],
         'BOOK_INFOR':['도서 정보1','도서 정보2','도서 정보3','도서 정보4'],
         'BOOK_RENT':[False,False,False,False],
         'BOOK_PIC':[None, None, None, None]})


#도서 csv 생성
BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')        #csv파일 생성 

f=open('BookList.csv','r',encoding='utf-8')
data=csv.reader(f) #data에 읽은 값 저장
#header=next(data) #csv파일의 1행 제거


#도서 검색
def BookSearch(): 
    Choice=input('도서 명, 저자, 출판사 : ')           #검색 기준 선택(도서 명, 저자, 출판사 중)
    if Choice=='도서 명':                             #도서 명 선택 시
        SearchIndex=0                                 #도서 데이터 다루기
    elif Choice=='저자':                              #저자 선택 시
        SearchIndex=2                                 #저자 데이터 다루기
    elif Choice=='출판사':                            #출판사 선택 시
        SearchIndex=3                                 #출판사 데이터 다루기
        
    Name=input("{} 입력 : ".format(Choice))          #검색값(도서 명) 입력
    print(BookField[0:6])          #필드명 출력
    for row in data:                 #도서 목록의 행만큼 반복
        if Name in row[SearchIndex]:#도서 목록의 첫 번째 행에 입력 값이 있다면
            print(row[0:6])          #해당 행에 해당하는 정보 출력
        elif Name == '':            #아무것도 입력하지 않을 시
            print(row[0:6])                 
     

#도서 등록
def BookSave():
    global BookDf
    Title=input("도서 명 : ")           #도서 명 입력
    Isbn=input("ISBN : ")               #ISBN 입력
    Author=input("저자 : ")             #저자 입력
    Pub=input("출판사 : ")              #출판사 입력
    Price=input("가격 : ")              #가격 입력
    Link=input("링크 : ")               #링크 입력
    Infor=input("도서 설명 : ")         #도서 설명 입력
    if '' in [Title,Isbn,Author, Pub, Price, Link, Infor]:        #입력값들로 리스트 생성 후 공백 있는 경우(정보값에 누락 O)
        print("올바른 값을 입력세요.")
    elif (BookDf['BOOK_ISBN']==Isbn).any():                       #등록 정보가 기존 데이터 값과 중복되는 경우
        print('중복된 도서입니다. 오류 : ISBN 중복')
    else:
        AddBookDf = pd.DataFrame({'BOOK_TITLE':[Title], 'BOOK_ISBN':[Isbn], 'BOOK_AUTHOR':[Author], 'BOOK_PUB':[Pub],       #입력값들로 데이터 프레임 생성
                                'BOOK_PRICE':[Price], 'BOOK_LINK':[Link],'BOOK_INFOR':[Infor], 'BOOK_RENT':[False],'BOOK_PIC':[None]})
        BookDf = pd.concat([BookDf, AddBookDf])                 #기존 데이터 프레임에 합치기
        BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')



#도서 수정
def BookAdit():
    ChangeTitle=input("변경할 도서 명 : ")   #수정하고자 하는 도서 선택
    if (BookDf['BOOK_TITLE']!=ChangeTitle).all():       #검색 결과가 없는 경우
        print('검색 결과가 없습니다.')
    else:
        Rent_Isbn= BookDf.loc[BookDf['BOOK_TITLE'].str.contains(ChangeTitle),('BOOK_ISBN')]                  ## 변경할 도서의 isbn
        Title=input("도서 명 ")                  #수정할 정보
        Isbn=input("ISBN ")                     #수정할 정보2
        if (BookDf['BOOK_ISBN']==Isbn).any():               #수정한 정보가 기존 데이터 값과 중복될 경우
            print('중복된 도서입니다. 오류 : ISBN 중복')
        else:
            BookDf.loc[BookDf['BOOK_TITLE'].str.contains(ChangeTitle),('BOOK_TITLE','BOOK_ISBN')]=(Title,Isbn)      #수정한 정보를 데이터 프레임에 추가
            BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')            #csv 파일에 수정 정보 추가

            if (RDf['BOOK_ISBN'] == Rent_Isbn[0]).any():                                                        ## isbn이 rent데이터프레임에 있을때
                RDf.loc[RDf['BOOK_ISBN'].str.contains(Rent_Isbn[0]), ('BOOK_ISBN')] = Isbn                      ## rent isbn을 변경할 isbn으로 바꿈

                RDf.to_csv('RentList.csv',index=False,encoding='utf-8')                                         ## 변경한 값으로csv 저장


#도서 삭제
def BookDel():
    global BookDf
    Title=input('삭제할 도서 명 ')           #삭제하고자 하는 도서 선택
    if BookDf.loc[BookDf['BOOK_TITLE'].str.contains(Title),('BOOK_RENT')].all()==True:      #대여 중인 경우(True)
        print('대여 중인 도서입니다.')
    else:
        Index = BookDf[BookDf['BOOK_TITLE'].str.contains(Title)].index            #삭제하고자 하는 도서 데이터의 인덱스 구하기
        BookDf = BookDf.drop(Index)                                               #해당 인덱스의 행 삭제
        BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')            #csv 파일에 삭제 정보 추가

    

#실행파일
#BookSave()
BookSearch()
#BookAdit()
#BookDel()
