from tkinter import *
from tkinter.ttk import *

Window=Tk()
Window.title('도서 관리 프로그램')
Window.geometry("800x500")       
Window.resizable(width = FALSE, height = FALSE)     #창 고정
#-m----Entry: c2, r1------
Search = Entry(Window, width=55)      #검색창 생성
Search.place(x=230, y=80)  #검색창 위치 지정
#-m----Menubar: c0, r0----
MainMenu = Menu(Window)
Window.config(menu = MainMenu)
fileMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "도서", menu = fileMenu)
MainMenu.add_cascade(label = "회원", menu = fileMenu)
MainMenu.add_cascade(label = "대여", menu = fileMenu)
MainMenu.add_cascade(label = "반납", menu = fileMenu)
#-m---- Combobox: c1, r1------
Combo = Combobox(Window, width=10)
Combo['values']=("도서 명", "저자", "출판사")   #검색 기준
Combo.current(0)                               #디폴트값 : 첫번째 값
Combo.pack()
Combo.place(x=130,y=80)
#-m----Listbox: c2, r2----
ListBox= Listbox(Window, width = 70, height = 17)
ListBox.insert(0,'List element1')
ListBox.insert(1,'List element2')
ListBox.place(x=130, y=110)

#등록 버튼
RegisterBotton=Button(Window,text='등록',command=Window.destroy)
RegisterBotton.place(x=230,y=50)

#검색 버튼
SearchBotton=Button(Window,text='검색',command=Window.destroy)
SearchBotton.place(x=630,y=80)

Window.mainloop()
