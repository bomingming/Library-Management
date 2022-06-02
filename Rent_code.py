import pandas as pd
from datetime import datetime, timedelta

RentDay = datetime.today().strftime('%Y-%m-%d')
ReturnDay = (datetime.today()+timedelta(14)).strftime('%Y-%m-%d')

UserDf = pd.read_csv('UserList.csv')        #회원 csv
BookDf = pd.read_csv('BookList.csv')        #도서 csv

RentDf = pd.DataFrame({'BOOK_ISBN':[], 'USER_PHONE':[], 'RENT_DATE':[], 'RENT_REDATE':[]})  #대여 데이터 프레임


#대여 
def RentBook():
    global RentDf
    RentBookIsbn = '9791170520634'      #대여하고자 하는 도서 ISBN
    RentUserPhone = '010-8523-7413'     #대여하고자 하는 회원 전화번호
    if BookDf.loc[BookDf['BOOK_ISBN'].str.contains(RentBookIsbn),('BOOK_RENT')].all()==False:     #도서가 대여중이 아닌 경우
        UserDf.loc[UserDf['USER_PHONE'].str.contains(RentBookIsbn), ('USER_RENT')]=True           #회원 대여 상태 True
        BookDf.loc[BookDf['BOOK_ISBN'].str.contains(RentBookIsbn),('BOOK_RENT')]=True             #도서 대여 상태 True
        AddRentDf = pd.DataFrame({'BOOK_ISBN':[RentBookIsbn], 'USER_PHONE':[RentUserPhone],             #데이터프레임에 대여 정보 추가
        'RENT_DATE':[RentDay], 'RENT_REDATE':[ReturnDay]})
        RentDf = pd.concat([RentDf, AddRentDf])                                                         #기존 데이터 프레임에 합치기
        RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')                                      #csv에 데이터 추가


#RentBook()


RentDf.to_csv('RentList.csv',index=False,encoding='utf-8') 