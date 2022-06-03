from tkinter import *
from tkinter.ttk import *


Window = Tk()


#디폴트 화면
DefaultLabel = Label(Window, text = "도서 관리 프로그램", font=("돋움체",25))      #대표 텍스트
DefaultLabel.place(x=230, y=190)                                                  #위젯 위치
SubLabel = Label(Window, text = "원하는 메뉴를 선택하세요.", font=("돋움체", 15))   #부제 텍스트
SubLabel.place(x=255, y=237)                                                      #위젯 위치





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


Window.mainloop()