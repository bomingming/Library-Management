from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd
from datetime import datetime, timedelta
from tkinter.filedialog import *
import math

NowDay = datetime.today().strftime('%Y-%m-%d')         #당일 날짜 표시
UserDf = pd.read_csv(r'.\UserList.csv')

#회원 세부 정보 함수
def UserInforwindow():
    Window = Tk()

    Window.title('회원 세부 정보')
    Window.geometry('700x450')
    Window.resizable(width = False, height = False)

    #텍스트
    NameLabel = Label(Window, text = '이름', font=('돋움체', 10))
    NameLabel.place(x = 410, y = 80)
    NameEnter = Entry(Window, width = 25)
    NameEnter.place(x = 450, y = 80)

    SexLabel = Label(Window, text = '성별', font = ('돋움체', 10))     # 성별
    SexLabel.place(x = 410, y = 115)

    var = IntVar()                                                                      # 성별 라디오버튼
    SexRadioButton1 = Radiobutton(Window, text = '남성', variable = var, value = 1)
    SexRadioButton1.place(x= 450, y = 115)
    SexRadioButton2 = Radiobutton(Window, text = '여성', variable = var, value = 2)
    SexRadioButton2.place(x = 500, y = 115)

    BirthLabel = Label(Window, text = '생년월일', font = ('돋움체', 10))    # 생년월일
    BirthLabel.place(x = 380, y = 150)
    BirthEnter = Entry(Window, width = 25)                            # 생년월일 텍스트
    BirthEnter.place(x = 450, y = 150)

    PhoneLabel = Label(Window, text = '전화번호', font = ('돋움체', 10))  # 전화번호
    PhoneLabel.place(x = 380, y = 185)
    PhoneEnter = Entry(Window, width = 25)                                # 전화번호 텍스트
    PhoneEnter.place(x = 450, y = 185)

    MailLabel = Label(Window, text = '이메일', font = ('돋움체', 10))   # 이메일
    MailLabel.place(x = 395, y = 220)
    MailEnter = Entry(Window, width = 25)                                # 이메일 텍스트
    MailEnter.place(x = 450, y = 220)


    def SelectPic():             # 이미지 파일열기 함수
        filename = askopenfilename(parent = Window, filetypes = (('GIF 파일','*gif'),('모든파일','*.*')))                       # [취소시 사진사라지는거]
        photo = PhotoImage(file = filename)
        ImageButton.configure(image = photo)
        ImageButton.image = photo

    ImageButton = Button(Window, text = '저장된 이미지가\n삭제되었거나 없습니다.', command = SelectPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

    def AddUser():  #회원 등록 누를 시
        global UserDf
        if (UserDf['USER_PHONE']==PhoneEnter.get()).any():
            messagebox.showerror('중복된 회원', '중복된 회원입니다. \n (오류 : ISBN 중복)')
        elif '' in [NameEnter.get(), BirthEnter.get(), PhoneEnter.get(), MailEnter.get()]:
            messagebox.showerror('등록 오류', '올바른 정보를 입력하세요.')

        else:
            AddUserDf = pd.DataFrame({'USER_NAME':[NameEnter.get()],        
         'USER_BIRTH':[BirthEnter.get()],
         'USER_PHONE':[PhoneEnter.get()],
         'USER_SEX':[bool(var)],               #True : 남성 / False : 여성
         'USER_MAIL':[MailEnter.get()],
         'USER_OUT':[None],             #탈퇴일 디폴트 값 : None
         'USER_IN':[NowDay],        #등록일 디폴트 값 : 오늘 날짜
         'USER_RENT':[False],           #대여 디폴트 값 : False.
         'USER_PIC':[None]})            #사진 디폴트 값 : None
            UserDf = pd.concat([UserDf, AddUserDf])         #등록 정보를 기존 데이터프레임에 합치기
            UserDf.to_csv('UserList.csv',index=False,encoding='utf-8')  #csv파일에 저장
            messagebox.showinfo('등록 완료', '등록이 완료되었습니다.')  #등록 완료 메시지

    #버튼
    OkButton = Button(Window, text = '등록', command=AddUser)      # 등록 버튼
    OkButton.place(x = 155, y = 290, width = 50)
    OutButton = Button(Window, text = '취소')                       # 취소 버튼
    OutButton.place(x = 230, y = 290, width = 50)




    Window.mainloop()
