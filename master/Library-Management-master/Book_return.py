#반납
from tkinter import Tk
import pandas as pd

root = Tk()

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

    #반납 검색 함수
def RETURN():
    
    


