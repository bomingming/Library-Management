from tkinter import *
from tkinter.ttk import *
import pandas as pd

BookDf = pd.read_csv('.\BookList.csv')

#도서 세부 정보 함수
def BookInfowindow(SelectBook):

    BIWindow = Tk()
    BIWindow.title('도서 세부 정보')
    BIWindow.geometry('700x450')
    BIWindow.resizable(width = False, height = False)

    for i in BookDf.index:
        if BookDf.loc[i,'BOOK_ISBN']==SelectBook:
            PrintBook=BookDf.loc[i]
    # 텍스트

    TitleLabel = Label(BIWindow, text = '도서 명', font=('돋움체', 10))    # 도서명
    TitleLabel.place(x = 390, y = 80)
    TitleEnter = Entry(BIWindow, width = 25)
    TitleEnter.place(x = 450, y = 80)
    TitleEnter.insert(0,PrintBook[0])

    AuthorLabel = Label(BIWindow, text = '저자', font=('돋움체', 10))    # 저자
    AuthorLabel.place(x = 410, y = 115)
    AuthorEnter = Entry(BIWindow, width = 25)                             # 저자 텍스트
    AuthorEnter.place(x = 450, y = 115)
    AuthorEnter.insert(0,PrintBook[2])

    PublishLabel = Label(BIWindow, text = '출판사', font = ('돋움체', 10))    # 출판사
    PublishLabel.place(x = 395, y = 150)
    PublishEnter = Entry(BIWindow, width = 25)                              # 출판사 텍스트
    PublishEnter.place(x = 450, y = 150)
    PublishEnter.insert(0,PrintBook[3])

    IsbnLabel = Label(BIWindow, text = 'ISBN', font = ('돋움체', 10))      # ISBN
    IsbnLabel.place(x = 410, y = 185)
    IsbnEnter = Entry(BIWindow, width = 25)                                # ISBN 텍스트
    IsbnEnter.place(x = 450, y = 185)
    IsbnEnter.insert(0,PrintBook[2])

    PriceLabel = Label(BIWindow, text = '가격', font = ('돋움체', 10))       # 가격  
    PriceLabel.place(x = 410, y = 220)
    PriceEnter = Entry(BIWindow, width = 25)                                # 가격 텍스트
    PriceEnter.place(x = 450, y = 220)
    PriceEnter.insert(0,PrintBook[4])

    LinkLabel = Label(BIWindow, text = '링크', font = ('돋움체', 10))       # 링크
    LinkLabel.place(x = 410, y = 255)
    LinkEnter = Entry(BIWindow, width = 25)                                 # 링크 텍스트
    LinkEnter.place(x = 450, y = 255)
    LinkEnter.insert(0,PrintBook[5])

    RentLabel = Label(BIWindow, text = '대여여부', font = ('돋움체', 10))      # 대여여부
    RentLabel.place(x = 380, y = 290)
    RentEnter = Entry(BIWindow, width = 25)                                     # 대여여부 텍스트
    RentEnter.place(x = 450, y = 290)
    RentEnter.insert(0,PrintBook[7])

    BookInfomationLabel = Label(BIWindow, text = '도서설명', font = ('돋움체', 10))   # 도서설명
    BookInfomationLabel.place(x = 380, y = 325)
    BookInfomationEnter = Text(BIWindow, width = 25, height = 5)                    # 도서 설명 텍스트
    BookInfomationEnter.insert(END,PrintBook[6])

    BookInfomationEnter.place(x = 450, y = 325)

    BIWindow.mainloop()