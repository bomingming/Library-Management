from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd

BookDf = pd.read_csv('BookList.csv')

#도서 세부 정보 함수
def CheckOrEdit(SelectBook):

    BIWindow = Tk()
    BIWindow.title('도서 세부 정보')
    BIWindow.geometry('700x450')
    BIWindow.resizable(width = False, height = False)

    for i in BookDf.index:
        if BookDf.loc[i,'BOOK_ISBN']==SelectBook:
            index=i
            PrintBook=BookDf.loc[index]
    print(PrintBook)
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

    # 버튼
    ImageButton = Button(BIWindow, image = '')                       # 도서 이미지 추가버튼
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)
    
    def Edit():  #도서 등록 버튼 누를 시
        global BookDf
        if (BookDf['BOOK_ISBN']==IsbnEnter.get()).any():
            messagebox.showerror('중복된 도서', '중복된 도서입니다. \n (오류 : ISBN 중복)') #등록 오류 메시지(중복)
        elif '' in [TitleEnter.get(),IsbnEnter.get(),AuthorEnter.get(), 
            AuthorEnter.get(), PriceEnter.get(), LinkEnter.get(),
            BookInfomationEnter.get(1.0, 50.50)]:
            messagebox.showerror('등록 오류', '올바른 정보를 입력하세요.')  #등록 오류 메시지(누락)

        else:
            BookDf.loc[index,0]=TitleEnter.get()
            BookDf.loc[index,1]=AuthorEnter.get()
            BookDf.loc[index,2]=PublishEnter.get()
            BookDf.loc[index,3]=IsbnEnter.get()
            BookDf.loc[index,4]=PriceEnter.get()
            BookDf.loc[index,5]=LinkEnter.get()
            BookDf.loc[index,6]=BookInfomationEnter.get(1.0, 50.50)

            BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')  #csv파일에 저장

            messagebox.showinfo('수정 완료', '수정이 완료되었습니다.')  #등록 완료 메시지
            BIWindow.destroy

    OkButton = Button(BIWindow, text = '확인', command=BIWindow.destroy)    # 확인 버튼
    OkButton.place(x = 130, y = 290, width = 50)

    OkButton = Button(BIWindow, text = '수정', command=Edit)                # 수정 버튼
    OkButton.place(x = 190, y = 290, width = 50)

    OutButton = Button(BIWindow, text = '취소',command=BIWindow.destroy)    # 취소 버튼
    OutButton.place(x = 250, y = 290, width = 50)
    
    BIWindow.mainloop()