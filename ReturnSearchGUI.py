from tkinter import *
from tkinter.ttk import *
import UserSearchGUI
import BookSearchGUI
import ReturnSearchGUI
import pandas as pd

def key():                         # 트리뷰 더블클릭 커멘드
    SelectBook = OutpuTreeview.focus()  #트리뷰에서 선택한 도서
    RealSelect = OutpuTreeview.item(SelectBook).get('values')
    print(RealSelect[1])    #선택한 도서의 ISBN(int값임)

def SearchResult():                    # 검색기준 선택, 검색이름 입력후 검색 클릭시 커멘드
    for i in OutpuTreeview.get_children():
        OutpuTreeview.delete(str(i))
    InStandard=Standard.get()           # 콤보박스의 입력값
    InSearch=SearchName.get()           # 검색창에 검색한 이름
    ResultSearch=(Search(InStandard,InSearch))
    for i in ResultSearch.index:
        PrintR=[]
        for j in ['BOOK_TITLE','BOOK_ISBN','BOOK_AUTHOR','BOOK_PUB','BOOK_RENT']:
            PrintR.append(ResultSearch.loc[i,j])
        OutpuTreeview.insert('','end',text=i,values=PrintR,iid=str(i))


# 도서 검색
def Search(InStandard,InSearch): 
    UserDf=pd.read_csv(r'.\UserList.csv')# data에 읽은 값 저장
    
    if InStandard=="회원 명":                  # 회원 명 선택 시
        SearchIndex="USER_NAME"               # 회원 데이터 다루기
    elif InStandard=="전화번호":                # 전화번호 선택 시
        SearchIndex="USER_PHONE"              # 회원 데이터 다루기

    if UserDf[SearchIndex].str.contains(InSearch).any():
        return UserDf.loc[UserDf[SearchIndex].str.contains(InSearch)]
    elif InSearch == '':
        return UserDf


def SearchWindow():
    Window=Tk()
    Window.title('도서 관리 프로그램')
    Window.geometry("800x500")
    Window.resizable(width = FALSE, height = FALSE)         # 창 고정

    def CrickBook():
        Window.destroy()
        BookSearchGUI.SearchWindow()

    def CrickUser():
        Window.destroy()
        UserSearchGUI.SearchWindow()

    def RentUser():
        Window.destroy()
        ReturnSearchGUI.SearchWindow()

    def ReturnUser():
        Window.destroy()
        BookSearchGUI.SearchWindow()
        
    #-m----Entry: c2, r1------
    global SearchName
    SearchName = Entry(Window, width=62)                    # 검색창 생성
    SearchName.place(x=230, y=80)                           # 검색창 위치 지정
    #-m----Menubar: c0, r0----
    MainMenu = Menu(Window)
    Window.config(menu = MainMenu)
    fileMenu = Menubutton(MainMenu)
    MainMenu.add_cascade(label = "도서", menu = fileMenu,command=CrickBook)
    MainMenu.add_cascade(label = "회원", menu = fileMenu,command=CrickUser)
    MainMenu.add_cascade(label = "대여", menu = fileMenu,command=RentUser)
    MainMenu.add_cascade(label = "반납", menu = fileMenu,command=ReturnUser)
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
    OutpuTreeview= Treeview(Window,columns=['제목','ISBN','저자','출판사','대여여부'])
    OutpuTreeview.column('#0',width=40,anchor='e')
    OutpuTreeview.heading('#0',text='번호',anchor='center')
    OutpuTreeview.column('#1',width=140,anchor='e')
    OutpuTreeview.heading('#1',text='제목',anchor='center')
    OutpuTreeview.column('#2',width=120,anchor='e')
    OutpuTreeview.heading('#2',text='ISBN',anchor='center')
    OutpuTreeview.column('#3',width=90,anchor='e')
    OutpuTreeview.heading('#3',text='저자',anchor='center')
    OutpuTreeview.column('#4',width=80,anchor='e')
    OutpuTreeview.heading('#4',text='출판사',anchor='center')
    
    OutpuTreeview.bind("<Double-Button-1>", key)  # 더블클릭시 key 커멘드 실행

    #등록 버튼
    RegisterBotton=Button(Window,text='등록',command=Window.destroy)
    RegisterBotton.place(x=230,y=50)

    #검색 버튼
    SearchBotton=Button(Window,text='⤶',command=SearchResult,width=2)
    SearchBotton.place(x=670,y=80)

    #대여 버튼
    SearchBotton=Button(Window,text='대여',command=SearchResult)
    SearchBotton.place(x=480,y=340)

    #반납 버튼
    SearchBotton=Button(Window,text='반납',command=SearchResult)
    SearchBotton.place(x=587,y=340)

    Window.mainloop()