from tkinter import *
from tkinter.ttk import *
import BookSearch
import pandas as pd

def key(event):                         # 트리뷰 더블클릭 커멘드
    SelectBook = OutpuTreeview.focus()  #트리뷰에서 선택한 도서
    RealSelect = OutpuTreeview.item(SelectBook).get('values')
    print(RealSelect[1])    #선택한 도서의 ISBN(int값임)

def SearchResult():   
    ResultSearch=pd.DataFrame()                  # 검색기준 선택, 검색이름 입력후 검색 클릭시 커멘드
    InStandard=Standard.get()           # 콤보박스의 입력값
    InSearch=SearchName.get()           # 검색창에 검색한 이름
    ResultSearch=(BookSearch.Search(InStandard,InSearch))
    for i in ResultSearch:
        PrintR=[]
        for j in ['BOOK_TITLE','BOOK_ISBN','BOOK_AUTHOR','BOOK_PUB','BOOK_RENT']:
            PrintR.append(ResultSearch.loc[i,j])
        OutpuTreeview.insert('','end',text=i,values=PrintR,iid=str(i))

def SearchWindow():
    Window=Tk()
    Window.title('도서 관리 프로그램')
    Window.geometry("800x500")
    Window.resizable(width = FALSE, height = FALSE)         # 창 고정
    #-m----Entry: c2, r1------
    global SearchName
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
    global Standard
    Standard = Combobox(Window, width=10,state='readonly')
        # state='readonly' 콤보 박스 글자 변경 제한
    Standard['values']=("도서 명", "저자", "출판사")   #검색 기준
    Standard.current(0)                               #디폴트값 : 첫번째 값
    Standard.pack()
    Standard.place(x=130,y=80)
    #-m----Listbox: c2, r2----
    global OutpuTreeview
    OutpuTreeview= Treeview(Window,columns=['제목','ISBN','저자','출판사'])
    OutpuTreeview.column('#0',width=40,anchor='e')
    OutpuTreeview.heading('#0',text='번호',anchor='center')
    OutpuTreeview.column('#1',width=140,anchor='e')
    OutpuTreeview.heading('#1',text='제목',anchor='center')
    OutpuTreeview.column('#2',width=160,anchor='e')
    OutpuTreeview.heading('#2',text='ISBN',anchor='center')
    OutpuTreeview.column('#3',width=90,anchor='e')
    OutpuTreeview.heading('#3',text='저자',anchor='center')
    OutpuTreeview.column('#4',width=110,anchor='e')
    OutpuTreeview.heading('#4',text='출판사',anchor='center')
    OutpuTreeview.place(x=130, y=110)
    OutpuTreeview.bind("<Double-Button-1>", key)  # 더블클릭시 key 커멘드 실행

    #등록 버튼
    RegisterBotton=Button(Window,text='등록',command=Window.destroy)
    RegisterBotton.place(x=230,y=50)

    #검색 버튼
    SearchBotton=Button(Window,text='검색',command=SearchResult)
    SearchBotton.place(x=630,y=80)

    Window.mainloop()

SearchWindow()