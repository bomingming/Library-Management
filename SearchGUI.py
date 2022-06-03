from tkinter import *
from tkinter.ttk import *
import BookSearch

def key(event):                     # 리스트 박스 더블클릭 커멘드
    a=OutputListBox.curselection()  # 더블클릭한 줄의 인덱스 출력
    b=OutputListBox.get(a)          # 리스트 박스의 인덱스 a의 값 출력
    print(b)

def SearchResult():                 # 검색기준 선택, 검색이름 입력후 검색 클릭시 커멘드
    InStandard=Standard.get()       # 콤보박스의 입력값
    InSearch=SearchName.get()           # 검색창에 검색한 이름
    ResultSearch=(BookSearch.Search(InStandard,InSearch))
    OutputListBox.insert(END,ResultSearch)

Window=Tk()
Window.title('도서 관리 프로그램')
Window.geometry("800x500")       
Window.resizable(width = FALSE, height = FALSE)     # 창 고정
#-m----Entry: c2, r1------
SearchName = Entry(Window, width=55)                    # 검색창 생성
SearchName.place(x=230, y=80)                           # 검색창 위치 지정
#-m----Menubar: c0, r0----
MainMenu = Menu(Window)
Window.config(menu = MainMenu)
fileMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "도서", menu = fileMenu)
MainMenu.add_cascade(label = "회원", menu = fileMenu)
MainMenu.add_cascade(label = "대여", menu = fileMenu)
MainMenu.add_cascade(label = "반납", menu = fileMenu)
#-m---- Combobox: c1, r1------
Standard = Combobox(Window, width=10,state='readonly')
    # state='readonly' 콤보 박스 글자 변경 제한
Standard['values']=("도서 명", "저자", "출판사")   #검색 기준
Standard.current(0)                               #디폴트값 : 첫번째 값
Standard.pack()
Standard.place(x=130,y=80)
#-m----Listbox: c2, r2----
OutputListBox= Listbox(Window, selectmode='browse', width = 70, height = 17)
OutputListBox.place(x=130, y=110)
OutputListBox.bind("<Double-Button-1>", key)  # 더블클릭시 key 커멘드 실행

#등록 버튼
RegisterBotton=Button(Window,text='등록',command=Window.destroy)
RegisterBotton.place(x=230,y=50)

#검색 버튼
SearchBotton=Button(Window,text='검색',command=SearchResult)
SearchBotton.place(x=630,y=80)

Window.mainloop()