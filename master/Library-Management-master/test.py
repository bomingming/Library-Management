from tkinter import *
from tkinter.ttk import *
import pandas as pd

#Window = Tk()


BookDf = pd.read_csv('.\BookList.csv')


#도서 세부 정보 함수
#def BookInfowindow():
BIWindow = Tk()

BIWindow.title('도서 세부 정보')
BIWindow.geometry('700x450')
BIWindow.resizable(width = False, height = False)

# 텍스트

TitleLabel = Label(BIWindow, text = '도서 명', font=('돋움체', 10))    # 도서명
TitleLabel.place(x = 390, y = 80)
TitleEnter = Entry(BIWindow, width = 25)    
AddTitle = TitleEnter.get()                          # 도서명 텍스트
TitleEnter.place(x = 450, y = 80)

AuthorLabel = Label(BIWindow, text = '저자', font=('돋움체', 10))    # 저자
AuthorLabel.place(x = 410, y = 115)
AuthorEnter = Entry(BIWindow, width = 25)                             # 저자 텍스트
AddAuthor = AuthorEnter.get()
AuthorEnter.place(x = 450, y = 115)


PublishLabel = Label(BIWindow, text = '출판사', font = ('돋움체', 10))    # 출판사
PublishLabel.place(x = 395, y = 150)
PublishEnter = Entry(BIWindow, width = 25)                              # 출판사 텍스트
AddPub = PublishEnter.get()
PublishEnter.place(x = 450, y = 150)

IsbnLabel = Label(BIWindow, text = 'ISBN', font = ('돋움체', 10))      # ISBN
IsbnLabel.place(x = 410, y = 185)
IsbnEnter = Entry(BIWindow, width = 25)                                # ISBN 텍스트
AddIsbn = IsbnEnter.get()
IsbnEnter.place(x = 450, y = 185)

PriceLabel = Label(BIWindow, text = '가격', font = ('돋움체', 10))       # 가격  
PriceLabel.place(x = 410, y = 220)
PriceEnter = Entry(BIWindow, width = 25)                                # 가격 텍스트
AddPrice = PriceEnter.get()
PriceEnter.place(x = 450, y = 220)

LinkLabel = Label(BIWindow, text = '링크', font = ('돋움체', 10))       # 링크
LinkLabel.place(x = 410, y = 255)
LinkEnter = Entry(BIWindow, width = 25)                                 # 링크 텍스트
AddLink = LinkEnter.get()
LinkEnter.place(x = 450, y = 255)

RentLabel = Label(BIWindow, text = '대여여부', font = ('돋움체', 10))      # 대여여부(추후 수정)
RentLabel.place(x = 380, y = 290)
RentEnter = Entry(BIWindow, width = 25)                                     # 대여여부 텍스트
AddRent = RentEnter.get()
RentEnter.place(x = 450, y = 290)

BookInfomationLabel = Label(BIWindow, text = '도서설명', font = ('돋움체', 10))   # 도서설명
BookInfomationLabel.place(x = 380, y = 325)
BookInfomationEnter = Text(BIWindow, width = 25, height = 5)                        # 도서 설명 텍스트
AddBInfor = BookInfomationEnter.get(1.0,-1.0)
BookInfomationEnter.place(x = 450, y = 325)

#새로 등록된 도서 정보
#AddList = [AddTitle, AddAuthor, AddPub, AddIsbn, AddPrice, AddLink, AddRent, AddBInfor]
AddDf = pd.DataFrame({'BOOK_TITLE':[AddTitle],
        'BOOK_ISBN':[AddIsbn],
        'BOOK_AUTHOR':[AddAuthor],
        'BOOK_PUB':[AddPub],
        'BOOK_PRICE':[AddPrice],
        'BOOK_LINK':[AddLink],
        'BOOK_INFOR':[AddBInfor],
        'BOOK_RENT':[False],
        'BOOK_PIC':[None]})
BookDf = pd.concat([BookDf, AddDf])

BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')





# 버튼
ImageButton = Button(BIWindow, image = '')                          # 도서 이미지 추가버튼
ImageButton.place(x = 130, y = 80, width = 170, height = 200)

OkButton = Button(BIWindow, text = '등록')                            # 등록 버튼
OkButton.place(x = 130, y = 290, width = 50)


OutButton = Button(BIWindow, text = '취소')                           # 삭제 버튼
OutButton.place(x = 250, y = 290, width = 50)



BIWindow.mainloop()

'''

Window.title("도서 관리 프로그램")      #프로그램 이름
Window.geometry("800x500")             #창 크기
Window.resizable(width = FALSE, height = FALSE)     #창 고정

MainMenu = Menu(Window)
Window.config(menu = MainMenu)

fileMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "도서", menu = fileMenu)
MainMenu.add_cascade(label = "회원", menu = fileMenu)
MainMenu.add_cascade(label = "대여", menu = fileMenu)
MainMenu.add_cascade(label = "반납", menu = fileMenu)
'''

#BookInfowindow()


#Window.mainloop()