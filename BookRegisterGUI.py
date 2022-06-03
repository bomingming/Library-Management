from tkinter import *
from tkinter.ttk import *

def BookRegister():       #등록 입력창
    RegisWindow = Tk()

    RegisWindow.title("도서 등록")          #새창 : 도서 등록
    RegisWindow.geometry("700x450")
    RegisWindow.resizable(width = FALSE, height = FALSE)

    TitleEnter = Entry(RegisWindow, width = 25)                     #도서 명 입력창
    TitleEnter.place(x=450, y=80)
    AuthorEnter = Entry(RegisWindow, width = 25)                    #저자 입력창
    AuthorEnter.place(x=450, y=115)
    PubEnter = Entry(RegisWindow, width = 25)                       #출판사 입력창
    PubEnter.place(x=450, y=150)
    IsbnEnter = Entry(RegisWindow, width = 25)                      #ISBN 입력창
    IsbnEnter.place(x=450, y=185)
    PriceEnter = Entry(RegisWindow, width = 25)      #가격 입력창
    PriceEnter.place(x=450, y=220)
    LinkEnter = Entry(RegisWindow, width = 25)       #링크 입력창
    LinkEnter.place(x=450, y=255)
    InforEnter = Text(RegisWindow, width = 25, height = 5)       #도서 설명 입력창
    InforEnter.place(x=450, y=290)

    TitleLabel = Label(RegisWindow, text = "도서 명", font=("돋움체",10))
    TitleLabel.place(x=390, y=80)
    AuthorLabel = Label(RegisWindow, text = "저자", font=("돋움체",10))
    AuthorLabel.place(x=410, y=115)
    PubLabel = Label(RegisWindow, text = "출판사", font=("돋움체",10))
    PubLabel.place(x=400, y=150)
    IsbnLabel = Label(RegisWindow, text = "ISBN", font=("돋움체",10))
    IsbnLabel.place(x=410, y=185)
    PriceLabel = Label(RegisWindow, text = "가격", font=("돋움체",10))
    PriceLabel.place(x=410, y=220)
    LinkLabel = Label(RegisWindow, text = "링크", font=("돋움체",10))
    LinkLabel.place(x=410, y=255)
    InforLabel = Label(RegisWindow, text = "도서 설명", font=("돋움체",10))
    InforLabel.place(x=375, y=290)

    #등록 버튼
    RegisterBotton=Button(RegisWindow,text='등록',command=RegisWindow.destroy)
    RegisterBotton.place(x=240,y=300)

    #취소 버튼
    CancelBotton=Button(RegisWindow,text='취소',command=RegisWindow.destroy)
    CancelBotton.place(x=100,y=300)

    RegisWindow.mainloop()
BookRegister()