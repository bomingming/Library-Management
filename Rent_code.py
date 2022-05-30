import pandas as pd
#from datetime import datetime, timedelta
import Book_code as Bc
import User_code as Uc

'''

RentDay = datetime.today().strftime('%Y-%m-%d')
ReturnDay = (datetime.today()+timedelta(14)).strftime('%Y-%m-%d')

RentDf = pd.DataFrame({'BOOK_ISBN':['9788937460449','9788937461668'], 'USER_PHONE':['010-1234-5678','010-9876-5432'],
                        'RENT_DATE':[RentDay, RentDay], 'RENT_REDATE':[ReturnDay, ReturnDay]})

'''


#대여 
def RentBook():
    global RentDf
    RentBookIsbn = '9791170520634'      #대여하고자 하는 도서 ISBN
    RentUserPhone = '010-8523-7413'     #대여하고자 하는 회원 전화번호
    if Bc.BookDf.loc[Bc.BookDf['BOOK_ISBN'].str.contains(RentBookIsbn),('BOOK_RENT')].all()==False:     #도서가 대여중이 아닌 경우
        Uc.UserDf.loc[Uc.UserDf['USER_PHONE'].str.contains(RentBookIsbn), ('USER_RENT')]=True           #회원 대여 상태 True
        Bc.BookDf.loc[Bc.BookDf['BOOK_ISBN'].str.contains(RentBookIsbn),('BOOK_RENT')]=True             #도서 대여 상태 True
        AddRentDf = pd.DataFrame({'BOOK_ISBN':[RentBookIsbn], 'USER_PHONE':[RentUserPhone],             #데이터프레임에 대여 정보 추가
        'RENT_DATE':[RentDay], 'RENT_REDATE':[ReturnDay]})
        RentDf = pd.concat([RentDf, AddRentDf])                                                         #기존 데이터 프레임에 합치기
        RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')                                      #csv에 데이터 추가


#반납
def ReturnBook():
    global RentDf
    RentBookIsbn = '9788937460449'
    if (RentBookIsbn == RentDf['BOOK_ISBN']).any():
        Index = RentDf[RentDf['BOOK_ISBN'].str.contains(RentBookIsbn)].index            #삭제하고자 하는 도서 데이터의 인덱스 구하기
        RentDf = RentDf.drop(Index)                                                     #해당 인덱스의 행 삭제
        RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')


#함수
#RentBook()
#ReturnBook()


RentDf.to_csv('RentList.csv',index=False,encoding='utf-8') 