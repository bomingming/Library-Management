from tkinter import *
from tkinter.ttk import *
import UserSearchGUI
import BookSearchGUI
import RentGUI
import UserInformationPrint
import pandas as pd
from tkinter import messagebox
from datetime import datetime, timedelta

NowDay = datetime.today().strftime('%Y-%m-%d')                          #오늘
ReturnDay = (datetime.today()+timedelta(days=14)).strftime('%Y-%m-%d')  #반납예정일

def ButtonClick(SelectBook, UIWindow, Window):
    RentDf = pd.read_csv('.\RentList.csv')
    UserDf = pd.read_csv(r'.\UserList.csv')
    BookDf = pd.read_csv('.\BookList.csv')

    SelectUser = OutpuTreeview.focus()  #트리뷰에서 선택한 회원
    SelectUser = OutpuTreeview.item(SelectUser).get('values')
    
    if SelectUser[4] != ' ':    #해당 회원이 탈퇴한 경우
        messagebox.showinfo('대여자 오류', '탈퇴한 회원입니다', master=UIWindow)
    else:
        RentBookIndex = BookDf[BookDf['BOOK_ISBN'] == SelectBook].index[0]

        BookDf = BookDf.astype({'BOOK_ISBN' : 'str' })
        UserDf = UserDf.astype({'USER_PHONE' : 'str' })

        answer = messagebox.askquestion('대여 완료', '대여하시겠습니까?\n회원 정보 : '+SelectUser[0]+
        '\n책 정보 : '+BookDf.loc[RentBookIndex,'BOOK_TITLE'])  #대여 의사 묻기
        if answer == 'yes':
            #대여 csv - 대여 도서 정보 추가
            AddDf = pd.DataFrame({'BOOK_ISBN':[SelectBook],   
            'USER_PHONE':[SelectUser[2]],
            'RENT_DATE':[NowDay],
            'RENT_REDATE':[ReturnDay]})
            RentDf = pd.concat([RentDf, AddDf])         #등록 정보를 기존 데이터프레임에 합치기
            RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')  #csv파일에 저장

            SelectBook = str(SelectBook)
            
            #도서 csv - 도서 대여 여부 변경
            BookDf.loc[BookDf['BOOK_ISBN'].str.contains(SelectBook), ['BOOK_RENT']] = '대출 중'
            BookDf.to_csv('BookList.csv', index = False, encoding = 'utf-8')

            #회원 csv - 회원 대여 여부 변경
            UserDf = UserDf.astype({'USER_RENT':int})
            UserDf.loc[UserDf['USER_PHONE'].str.contains(SelectUser[2]), ['USER_RENT']] += 1    # +=1
            UserDf.to_csv('UserList.csv', index = False, encoding = 'utf-8')

            messagebox.showinfo('대여완료', '대여가 완료되었습니다.\n대여일 : '+NowDay+
            '\n반납예정일 : '+ReturnDay, master=UIWindow)

    UIWindow.destroy()  #회원 목록 창 제거
    Window.destroy()    #도서 세부 정보 창 제거


def SearchResult():                     # 검색기준 선택, 검색이름 입력후 검색 클릭시 커멘드
    for i in OutpuTreeview.get_children():
        OutpuTreeview.delete(str(i))
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


def SearchWindow(SelectBook, Window):
    UIWindow=Tk()
    UIWindow.title('회원 관리 프로그램')
    UIWindow.geometry("700x400")
    UIWindow.resizable(width = FALSE, height = FALSE)         # 창 고정

    #-m----Entry: c2, r1------
    global SearchName
    SearchName = Entry(UIWindow, width=55)                    # 검색창 생성
    SearchName.place(x=190, y=60)                           # 검색창 위치 지정

    global Standard
    Standard = Combobox(UIWindow, width=10,state='readonly')
    # state='readonly' 콤보 박스 글자 변경 제한
    Standard['values']=("회원 명", "전화번호")   #검색 기준
    Standard.current(0)                               #디폴트값 : 첫번째 값
    Standard.pack()
    Standard.place(x=90,y=60)
    #-m----Listbox: c2, r2----
    global OutpuTreeview
    OutpuTreeview= Treeview(UIWindow,columns=['회원 명','생일','전화번호','성별','탈퇴일'])
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
    OutpuTreeview.place(x=90, y=90)

    #검색 버튼
    SearchBotton=Button(UIWindow,text="⤶",command=SearchResult,width=2)
    SearchBotton.place(x=580,y=58)

    #선택 버튼
    RegisterBotton=Button(UIWindow,text='선택',command=lambda : ButtonClick(SelectBook, UIWindow,Window))
    RegisterBotton.place(x=495,y=320)

    UIWindow.mainloop()