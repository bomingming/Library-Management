from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import UserSearchGUI
import BookSearchGUI
import ReturnSearchGUI
import RentGUI
import pandas as pd

UserDf=pd.read_csv(r'.\UserList.csv')# data에 읽은 값 저장
RentDf=pd.read_csv(r'.\RentList.csv')# data에 읽은 값 저장
BookDf=pd.read_csv(r'.\BookList.csv')# data에 읽은 값 저장

def TreeviesDrop():
    for i in OutpuTreeview.get_children(): # 트리뷰 입력된값 삭제
        OutpuTreeview.delete(str(i))

def SearchResult():                    # 검색기준 선택, 검색이름 입력후 검색 클릭시 커멘드

    UserDf=pd.read_csv(r'.\UserList.csv')# data에 읽은 값 저장
    RentDf=pd.read_csv(r'.\RentList.csv')# data에 읽은 값 저장
    BookDf=pd.read_csv(r'.\BookList.csv')# data에 읽은 값 저장

    TreeviesDrop()

    InStandard=Standard.get()           # 콤보박스의 입력값
    InSearch=SearchName.get()           # 검색창에 검색한 이름

    for i in RentDf.values:
        PrintR=[]
        for j in UserDf.values:
            if j[2]==i[1]:
                PrintR.append(j[0])
                PrintR.append(j[2])
        for j in BookDf.values:
            if j[1]==i[0]:
                PrintR.append(j[0])
        PrintR.append(i[2])
        PrintR.append(i[3])
        if InStandard=='회원 명':
            if InSearch in PrintR[0]:
                OutpuTreeview.insert('','end',text=i,values=PrintR,iid=str(i))
        elif InStandard=='도서 명':
            if InSearch in PrintR[2]:
                OutpuTreeview.insert('','end',text=i,values=PrintR,iid=str(i))
        elif InSearch=='':
            OutpuTreeview.insert('','end',text=i,values=PrintR,iid=str(i))

def ReturnBotton():
    SelectBook = OutpuTreeview.focus()  #트리뷰에서 선택한 도서
    SelectBook = OutpuTreeview.item(SelectBook).get('values')
    BookName = SelectBook[2]
    BookISBN = BookDf.loc[BookDf['BOOK_TITLE'].str.contains(BookName),['BOOK_ISBN']]
    UserPhone = SelectBook[1]
    UserName = SelectBook[0]
    TreeviesDrop()

    answer = messagebox.askquestion('반납완료','반납하시겠습니까?\n회원 정보 : '+UserName+
    '\n책 정보 : '+BookName)  #대여 의사 묻기
    if answer == 'yes':
        DropIndex=RentDf[RentDf['BOOK_ISBN'] == BookISBN].index[0]
        RentDf1=RentDf.drop(DropIndex)

        UserDf.loc[UserDf['USER_PHONE'].str.contains(UserPhone),['USER_RENT']]=(
            UserDf.loc[UserDf['USER_PHONE'].str.contains(UserPhone),['USER_RENT']]-1)
        BookDf.loc[BookDf['BOOK_TITLE'].str.contains(BookName),['BOOK_RENT']]='미대여'

        UserDf.to_csv('UserList.csv',index=False,encoding='utf-8')  #csv파일에 저장
        BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')  #csv파일에 저장
        RentDf1.to_csv('RentList.csv',index=False,encoding='utf-8')  #csv파일에 저장


def SearchWindow():
    Window=Tk()
    Window.title('반납 프로그램')
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
        RentGUI.SearchWindow()

    def ReturnUser():
        Window.destroy()
        ReturnSearchGUI.SearchWindow()
        
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
    Standard['values']=("회원 명","도서 명")   #검색 기준
    Standard.current(0)                               #디폴트값 : 첫번째 값
    Standard.pack()
    Standard.place(x=130,y=80)
    #-m----Listbox: c2, r2----
    global OutpuTreeview
    OutpuTreeview= Treeview(Window,columns=['대여자','전화번호','도서 제목','대여일','반납일'])
    OutpuTreeview.column('#0',width=0,anchor='e')
    OutpuTreeview.heading('#0',text='',anchor='center')
    OutpuTreeview.column('#1',width=50,anchor='e')
    OutpuTreeview.heading('#1',text='대여자',anchor='center')
    OutpuTreeview.column('#2',width=105,anchor='e')
    OutpuTreeview.heading('#2',text='전화번호',anchor='center')
    OutpuTreeview.column('#3',width=140,anchor='e')
    OutpuTreeview.heading('#3',text='도서 제목',anchor='center')
    OutpuTreeview.column('#4',width=120,anchor='e')
    OutpuTreeview.heading('#4',text='대여일',anchor='center')
    OutpuTreeview.column('#5',width=120,anchor='e')
    OutpuTreeview.heading('#5',text='반납일',anchor='center')
    OutpuTreeview.place(x=130, y=110)

    #검색 버튼
    SearchBotton=Button(Window,text='⤶',command=SearchResult,width=2)
    SearchBotton.place(x=670,y=80)

    #반납 버튼
    SearchBotton=Button(Window,text='반납',command=ReturnBotton)
    SearchBotton.place(x=587,y=340)
    TreeviesDrop()

    Window.mainloop()