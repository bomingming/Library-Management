import pandas as pd
from datetime import datetime, timedelta
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

'''
'''
Window = Tk()


RentDay = datetime.today().strftime('%Y-%m-%d')                     #대여일
ReturnDay = (datetime.today()+timedelta(14)).strftime('%Y-%m-%d')   #반납예정일

UserDf = pd.read_csv('UserList.csv')        #회원 csv
BookDf = pd.read_csv('BookList.csv')        #도서 csv

RentDf = pd.DataFrame({'BOOK_ISBN':[], 'USER_PHONE':[], 'RENT_DATE':[], 'RENT_REDATE':[]})  #대여 데이터 프레임


#대여 함수
def RentBook():

    def SearchBar():                          #검색창 함수
        Search = Entry(Window, width=52)      #검색창 생성
        Search.place(x=230, y=80)             #검색창 위치 지정


    def SearchList():                                                           #검색 목록 함수
        SearchList = Listbox(Window, selectmode='single', width=70, height=14)  #single : 단일 선택, 방향키 이동 후 스페이스바로 선택
        SearchList.insert(0, "1")                                               #(이벤트 처리 필요) 임의의 목록 값
        SearchList.place(x=130, y=130)


    def SearchCombo():                                         #검색 기준 함수
        Combo = Combobox(Window, width=10, state='readonly')
        Combo['values']=("도서 명", "저자", "출판사")           #검색 기준
        Combo.current(0)                                       #디폴트값 : 첫번째 값
        Combo.pack()
        Combo.place(x=130,y=80)


    def BookSelect():           #대여하고자 하는 도서 선택 시

        NewWindow = Tk()

        NewWindow.title("도서 세부 정보")                              #새창 : 도서 세부 정보
        NewWindow.geometry("700x450")
        NewWindow.resizable(width = FALSE, height = FALSE)

        TitleEnter = Entry(NewWindow, width = 25)                     #도서 명 입력창
        TitleEnter.place(x=450, y=80)
        AuthorEnter = Entry(NewWindow, width = 25)                    #저자 입력창
        AuthorEnter.place(x=450, y=115)
        PubEnter = Entry(NewWindow, width = 25)                       #출판사 입력창
        PubEnter.place(x=450, y=150)
        IsbnEnter = Entry(NewWindow, width = 25)                      #ISBN 입력창
        IsbnEnter.place(x=450, y=185)
        PriceEnter = Entry(NewWindow, width = 25)      #가격 입력창
        PriceEnter.place(x=450, y=220)
        LinkEnter = Entry(NewWindow, width = 25)       #링크 입력창
        LinkEnter.place(x=450, y=255)
        InforEnter = Text(NewWindow, width = 25, height = 5)       #도서 설명 입력창
        InforEnter.place(x=450, y=290)

        TitleLabel = Label(NewWindow, text = "도서 명", font=("돋움체",10))
        TitleLabel.place(x=390, y=80)
        AuthorLabel = Label(NewWindow, text = "저자", font=("돋움체",10))
        AuthorLabel.place(x=410, y=115)
        PubLabel = Label(NewWindow, text = "출판사", font=("돋움체",10))
        PubLabel.place(x=400, y=150)
        IsbnLabel = Label(NewWindow, text = "ISBN", font=("돋움체",10))
        IsbnLabel.place(x=410, y=185)
        PriceLabel = Label(NewWindow, text = "가격", font=("돋움체",10))
        PriceLabel.place(x=410, y=220)
        LinkLabel = Label(NewWindow, text = "링크", font=("돋움체",10))
        LinkLabel.place(x=410, y=255)
        InforLabel = Label(NewWindow, text = "도서 설명", font=("돋움체",10))
        InforLabel.place(x=375, y=290)

        BookImage = Button(NewWindow, image = '')                              #도서 이미지 버튼
        BookImage.place(x = 130, y = 80, width = 170, height = 200)

        OkButton = Button(NewWindow, text = '대여')                            #대여 버튼
        OkButton.place(x = 130, y = 290, width = 50)

        EditButton = Button(NewWindow, text = '대여자')                        #대여자 버튼
        EditButton.place(x = 190, y = 290, width = 50)

        OutButton = Button(NewWindow, text = '취소')                           #취소 버튼
        OutButton.place(x = 250, y = 290, width = 50)


        NewWindow.mainloop()


'''
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


#대여자를 선택하지 않고 대여 시도 시
messagebox.showerror('대여 오류', '대여자를 선택해주세요.')

#대여자 선택 후 대여 시도 시
messagebox.askquestion('대여', '대여하시겠습니까?\n회원 정보: \n책: ')

#대여 완료 시
messagebox.showinfo('대여 완료', '대여 완료되었습니다.\n대여기간: ')



RentBook()



RentDf.to_csv('RentList.csv',index=False,encoding='utf-8') 