from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pandas as pd

BookDf=pd.read_csv('BookList.csv')

RETURNwindow = Tk()
RETURNwindow.geometry('700x450')
RETURNwindow.title("책 반납")
RETURNwindow.resizable(width = False, height = False)
#반납 메뉴 선택시

def Default():      #기본 화면 함수
    DefaultLabel = Label(RETURNwindow, text = "도서 관리 프로그램", font=("돋움체",25))      #대표 텍스트
    DefaultLabel.place(x=220, y=140)                                                  #위젯 위치
    SubLabel = Label(RETURNwindow, text = "원하는 메뉴를 선택하세요.", font=("돋움체", 15))   #부제 텍스트
    SubLabel.place(x=225, y=237)                                                      #위젯 위치


  
Search = Entry(RETURNwindow, width=50)      #검색창 생성
Search.place(x=200, y=200)  #검색창 위치 지정
# Search.pack()

#검색 엔터 버튼
EnterButton = Button(RETURNwindow, text="⤶", width = 2)
EnterButton.place(x=550, y=200)

 #검색 기준 콤보박스
Combo = Combobox(RETURNwindow, width=10)
Combo['values']=("도서 명", "저자", "출판사")   #검색 기준
Combo.current(0)                               #디폴트값 : 첫번째 값
Combo.grid(row=1, column=1)                    #위젯 순서
Combo.place(x=130,y=200)  

#각 values값에 따른 if 로 나뉘어 검색진행 -> in rentDf 에서의 검색 진행
#default 도서명 선택하고 검색
if(BookDf['BOOK_RENT']!=Search.get()).any():
     messagebox.showerror('반납도서', '이미 반납된 도서입니다. ')


        






Default()
'''
SearchBar()
BookSearchType()
SearchEnter()
'''
RETURNwindow.mainloop()
