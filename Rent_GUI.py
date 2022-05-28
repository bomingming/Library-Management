from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox


Window = Tk()



def RentBookInfor():    #도서 세부 정보 창
    RentInfor = Tk()

    RentInfor.title("도서 세부 정보")          #새창 : 도서 세부 정보
    RentInfor.geometry("630x400")
    RentInfor.resizable(width = FALSE, height = FALSE)


    TitleEnter = Entry(RentInfor, width = 25)                     #도서 명 입력창
    TitleEnter.place(x=400, y=50)
    AuthorEnter = Entry(RentInfor, width = 25)                    #저자 입력창
    AuthorEnter.place(x=400, y=85)
    PubEnter = Entry(RentInfor, width = 25)                       #출판사 입력창
    PubEnter.place(x=400, y=120)
    IsbnEnter = Entry(RentInfor, width = 25)                      #ISBN 입력창
    IsbnEnter.place(x=400, y=155)
    PriceEnter = Entry(RentInfor, width = 25)                     #가격 입력창
    PriceEnter.place(x=400, y=190)
    LinkEnter = Entry(RentInfor, width = 25)                      #링크 입력창
    LinkEnter.place(x=400, y=225)
    InforEnter = Text(RentInfor, width = 25, height = 6)          #도서 설명 입력창
    InforEnter.place(x=400, y=260)

    TitleLabel = Label(RentInfor, text = "도서 명", font=("돋움체",10))
    TitleLabel.place(x=340, y=50)
    AuthorLabel = Label(RentInfor, text = "저자", font=("돋움체",10))
    AuthorLabel.place(x=360, y=85)
    PubLabel = Label(RentInfor, text = "출판사", font=("돋움체",10))
    PubLabel.place(x=350, y=120)
    IsbnLabel = Label(RentInfor, text = "ISBN", font=("돋움체",10))
    IsbnLabel.place(x=360, y=155)
    PriceLabel = Label(RentInfor, text = "가격", font=("돋움체",10))
    PriceLabel.place(x=360, y=190)
    LinkLabel = Label(RentInfor, text = "링크", font=("돋움체",10))
    LinkLabel.place(x=360, y=225)
    InforLabel = Label(RentInfor, text = "도서 설명", font=("돋움체",10))
    InforLabel.place(x=325, y=260)

    BookPhoto = Button(RentInfor, width = 23, height = 14)      #도서 이미지 버튼
    BookPhoto.grid(row=0, column=0)
    BookPhoto.place(x=100, y=50)
    #이미지 넣는 코드 추가 필요

    RentButton = Button(RentInfor, width = 5, text="대여")          #대여 버튼
    RentButton.pack()
    RentButton.place(x=115, y=280)

    UserButton = Button(RentInfor, width = 5, text="대여자")          #대여자 버튼
    UserButton.pack()
    UserButton.place(x=165, y=280)

    cancelButton = Button(RentInfor, width = 5, text="취소")          #취소 버튼
    cancelButton.pack()
    cancelButton.place(x=215, y=280)

    RentInfor.mainloop()




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


RentBookInfor()



#대여자를 선택하지 않고 ‘대여’ 버튼을 누를 경우
messagebox.showwarning("대여 오류", "대여자를 선택해주세요.")


#대여자 선택 후 ‘대여’ 버튼 누를 경우
messagebox.askyesno("대여 확정", "대여 하시겠습니까?\n회원 정보: \n책:")


#대여 완료 시
messagebox.showinfo("대여 완료", "대여가 완료되었습니다.\n대여 기간: ")


Window.mainloop()

