from tkinter import *
from tkinter.ttk import *
import UserSearchGUI
import BookSearchGUI
import ReturnSearchGUI
import RentGUI
import UserInformationPrint
import UserRegisterButton
import pandas as pd

def TreeviewDrop():
    for i in OutpuTreeview.get_children(): # 트리뷰 입력된값 삭제
        OutpuTreeview.delete(str(i))

def ButtonClick():
    SelectBook = OutpuTreeview.focus()  #트리뷰에서 선택한 회원
    SelectBook = OutpuTreeview.item(SelectBook).get('values')
    SelectBook = SelectBook[2]
    TreeviewDrop()
    UserInformationPrint.UserInfowindow(SelectBook)

def SearchResult():                     # 검색기준 선택, 검색이름 입력후 검색 클릭시 커멘드
    TreeviewDrop()
    InStandard=Standard.get()           # 콤보박스의 입력값
    InSearch=SearchName.get()           # 검색창에 검색한 이름
    ResultSearch=(Search(InStandard,InSearch))
    for i in ResultSearch.index:
        PrintR=[]
        for j in ['USER_NAME','USER_BIRTH','USER_PHONE','USER_SEX','USER_OUT']:
            if ResultSearch.loc[i,j]==False:
                PrintR.append('여성')
            elif ResultSearch.loc[i,j]==True:
                PrintR.append('남성')
            elif pd.isna(ResultSearch.loc[i,j]) == True:
                PrintR.append('')
            else:
                PrintR.append(ResultSearch.loc[i,j])
        OutpuTreeview.insert('','end',text=i,values=PrintR,iid=str(i))
    


# 회원 검색
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
    Window.title('회원 관리 프로그램')
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
    SearchName = Entry(Window, width=55)                    # 검색창 생성
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
    Standard['values']=("회원 명", "전화번호")   #검색 기준
    Standard.current(0)                               #디폴트값 : 첫번째 값
    Standard.pack()
    Standard.place(x=130,y=80)
    #-m----Listbox: c2, r2----
    global OutpuTreeview
    OutpuTreeview= Treeview(Window,columns=['회원 명','생일','전화번호','성별','탈퇴일'])
    OutpuTreeview.column('#0',width=70,anchor='e')
    OutpuTreeview.heading('#0',text='회원 번호',anchor='center')
    OutpuTreeview.column('#1',width=80,anchor='e')
    OutpuTreeview.heading('#1',text='회원 명',anchor='center')
    OutpuTreeview.column('#2',width=90,anchor='e')
    OutpuTreeview.heading('#2',text='생일',anchor='center')
    OutpuTreeview.column('#3',width=110,anchor='e')
    OutpuTreeview.heading('#3',text='전화번호',anchor='center')
    OutpuTreeview.column('#4',width=50,anchor='e')
    OutpuTreeview.heading('#4',text='성별',anchor='center')
    OutpuTreeview.column('#5',width=90,anchor='e')
    OutpuTreeview.heading('#5',text='탈퇴일',anchor='center')
    OutpuTreeview.place(x=130, y=110)

    #등록 버튼
    RegisterBotton=Button(Window,text='등록',command=UserRegisterButton.UserInforwindow)
    RegisterBotton.place(x=230,y=50)

    #검색 버튼
    SearchBotton=Button(Window,text="⤶",command=SearchResult,width=2)
    SearchBotton.place(x=620,y=79)

    #검색 및 수정 버튼
    RegisterBotton=Button(Window,text='확인 및 수정',command=ButtonClick)
    RegisterBotton.place(x=535,y=340)

    Window.mainloop()
