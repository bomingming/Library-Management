#반납
import pandas as pd
def ReturnBook():
    Userdf = pd.read_csv('UserList.csv')
    Bookdf = pd.read_csv('BookList.csv')

    #대여한 csv파일 열기
    f=open('BookList.csv','r',encoding='utf-8')

    RentBookIsbn = '9788937460449'
    if (RentBookIsbn in Bookdf["BOOK_RENT"]):
        INDEX = Bookdf[Bookdf["BOOK_ISBN"].str.contains(RentBookIsbn)].index
        Bookdf = Bookdf.drop(INDEX)
        Bookdf.to_csv('BOOK_RENT',index=True,encoding='utf-8')      
        Userdf.to_csv('USER_RENT',index=True,encoding='utf-8')




    # if (RentBookIsbn == RentDf['BOOK_ISBN']).any():
    #     Index = RentDf[RentDf['BOOK_ISBN'].str.contains(RentBookIsbn)].index            #삭제하고자 하는 도서 데이터의 인덱스 구하기
    #     RentDf = RentDf.drop(Index)                                                     #해당 인덱스의 행 삭제
    #     RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')
