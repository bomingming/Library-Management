#도서 검색 GUI

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


Window = Tk()


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


def CheckButton():      #수정 및 확인 버튼 함수
    CheckButton = Button(Window, text = "수정 및 확인")
    CheckButton.place(x=535, y=365) 


def SearchEnter():      #검색 엔터 버튼 함수
    EnterButton = Button(Window, text="⤶", width = 2)
    EnterButton.place(x=586, y=78)




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


#검색어와 일치하는 결과가 없는 경우
messagebox.showerror('중복된 도서', '중복된 도서입니다. \n (오류 : ISBN 중복)')



SearchBar()     #검색창
SearchList()    #검색 목록
SearchCombo()   #검색 기준
CheckButton()   #수정 및 확인
SearchEnter()   #검색 엔터 버튼 함수



Window.mainloop()