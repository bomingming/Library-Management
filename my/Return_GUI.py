from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

RETURNwindow = Tk()
RETURNwindow.geometry('700x450')
RETURNwindow.title("책 반납")
RETURNwindow.resizable(width = False, height = False)
#반납 메뉴 선택시

def Default():      #기본 화면 함수
    DefaultLabel = Label(RETURNwindow, text = "도서 관리 프로그램", font=("돋움체",25))      #대표 텍스트
    DefaultLabel.place(x=230, y=190)                                                  #위젯 위치
    SubLabel = Label(RETURNwindow, text = "원하는 메뉴를 선택하세요.", font=("돋움체", 15))   #부제 텍스트
    SubLabel.place(x=255, y=237)                                                      #위젯 위치


def SearchBar():         #검색창 함수
    Search = Entry(RETURNwindow, width=55)      #검색창 생성
    Search.place(x=230, y=200)  #검색창 위치 지정


def BookSearchType():  #검색 기준 콤보박스 함수
    Combo = Combobox(RETURNwindow, width=10)
    Combo['values']=("도서 명", "저자", "출판사")   #검색 기준
    Combo.current(0)                               #디폴트값 : 첫번째 값
    Combo.grid(row=1, column=1)                    #위젯 순서
    Combo.place(x=130,y=200)  
