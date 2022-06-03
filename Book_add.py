from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd

Window = Tk()


BookDf = pd.read_csv('.\BookList.csv')


#도서 세부 정보 함수
def BookInfowindow():
    BIWindow = Tk()

    BIWindow.title('도서 세부 정보')
    BIWindow.geometry('700x450')
    BIWindow.resizable(width = False, height = False)

    # 텍스트

    TitleLabel = Label(BIWindow, text = '도서 명', font=('돋움체', 10))    # 도서명
    TitleLabel.place(x = 390, y = 80)
    TitleEnter = Entry(BIWindow, width = 25)    
    TitleEnter.place(x = 450, y = 80)

    AuthorLabel = Label(BIWindow, text = '저자', font=('돋움체', 10))    # 저자
    AuthorLabel.place(x = 410, y = 115)
    AuthorEnter = Entry(BIWindow, width = 25)                             # 저자 텍스트
    AuthorEnter.place(x = 450, y = 115)


    PublishLabel = Label(BIWindow, text = '출판사', font = ('돋움체', 10))    # 출판사
    PublishLabel.place(x = 395, y = 150)
    PublishEnter = Entry(BIWindow, width = 25)                              # 출판사 텍스트
    PublishEnter.place(x = 450, y = 150)

    IsbnLabel = Label(BIWindow, text = 'ISBN', font = ('돋움체', 10))      # ISBN
    IsbnLabel.place(x = 410, y = 185)
    IsbnEnter = Entry(BIWindow, width = 25)                                # ISBN 텍스트
    IsbnEnter.place(x = 450, y = 185)

    PriceLabel = Label(BIWindow, text = '가격', font = ('돋움체', 10))       # 가격  
    PriceLabel.place(x = 410, y = 220)
    PriceEnter = Entry(BIWindow, width = 25)                                # 가격 텍스트
    PriceEnter.place(x = 450, y = 220)

    LinkLabel = Label(BIWindow, text = '링크', font = ('돋움체', 10))       # 링크
    LinkLabel.place(x = 410, y = 255)
    LinkEnter = Entry(BIWindow, width = 25)                                 # 링크 텍스트
    LinkEnter.place(x = 450, y = 255)

    RentLabel = Label(BIWindow, text = '대여여부', font = ('돋움체', 10))      # 대여여부
    RentLabel.place(x = 380, y = 290)
    RentEnter = Entry(BIWindow, width = 25)                                     # 대여여부 텍스트
    RentEnter.place(x = 450, y = 290)

    BookInfomationLabel = Label(BIWindow, text = '도서설명', font = ('돋움체', 10))   # 도서설명
    BookInfomationLabel.place(x = 380, y = 325)
    BookInfomationEnter = Text(BIWindow, width = 25, height = 5)                        # 도서 설명 텍스트

    BookInfomationEnter.place(x = 450, y = 325)
    
    def AddBook():  #도서 등록 버튼 누를 시
        global BookDf
        if (BookDf['BOOK_ISBN']==IsbnEnter.get()).any():
            messagebox.showerror('중복된 도서', '중복된 도서입니다. \n (오류 : ISBN 중복)')
        elif '' in [TitleEnter.get(),IsbnEnter.get(),AuthorEnter.get(), 
            AuthorEnter.get(), PriceEnter.get(), LinkEnter.get(),
            BookInfomationEnter.get(1.0, 50.50)]:
            messagebox.showerror('등록 오류', '올바른 정보를 입력하세요.')

        else:
            AddDf = pd.DataFrame({'BOOK_TITLE':[TitleEnter.get()],
                'BOOK_ISBN':[IsbnEnter.get()],
                'BOOK_AUTHOR':[AuthorEnter.get()],
                'BOOK_PUB':[AuthorEnter.get()],
                'BOOK_PRICE':[PriceEnter.get()],
                'BOOK_LINK':[LinkEnter.get()],
                'BOOK_INFOR':[BookInfomationEnter.get(1.0, 50.50)],
                'BOOK_RENT':[False],
                'BOOK_PIC':[None]})
            BookDf = pd.concat([BookDf, AddDf])

            BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')

    # 버튼
    ImageButton = Button(BIWindow, image = '')                          # 도서 이미지 추가버튼
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

    OkButton = Button(BIWindow, text = '등록', command=AddBook)                            # 확인 버튼
    OkButton.place(x = 130, y = 290, width = 50)

    OutButton = Button(BIWindow, text = '취소')                           # 삭제 버튼
    OutButton.place(x = 250, y = 290, width = 50)
    
    BIWindow.mainloop()




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


BookInfowindow()


Window.mainloop()