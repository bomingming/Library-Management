from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd
from datetime import datetime, timedelta
from tkinter.filedialog import *
import math
from PIL import ImageTk
from PIL import Image

NowDay = datetime.today().strftime('%Y-%m-%d')         #당일 날짜 표시
UserDf = pd.read_csv(r'.\UserList.csv')
PutSex=True
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

    def man():
        global PutSex
        PutSex=True

    def woman():
        global PutSex
        PutSex=False

    SexRadioButton1 = Radiobutton(Window, text = '남성', value=1,command=man)
    SexRadioButton1.place(x= 450, y = 115)
    SexRadioButton2 = Radiobutton(Window, text = '여성',value=2, command=woman)
    SexRadioButton2.place(x = 500, y = 115)

    year = [str(i) for i in range(1950, 2051)]
    month = [str(i).zfill(2) for i in range(1, 13)]
    day = [str(i).zfill(2) for i in range(1, 32)]

    BirthLabel = Label(Window, text = '생년월일', font = ('돋움체', 10))                 # 생년월일
    BirthLabel.place(x = 380, y = 150)
    YearCombo = Combobox(Window, width = 4, height = 15, values = year)
    YearCombo.configure(state = 'readonly')
    YearLabel = Label(Window, text = '년', font = ('돋움체', 10))
    MonthCombo = Combobox(Window, width = 2, height = 10, values = month)
    MonthCombo.configure(state = 'readonly')
    MonthLabel = Label(Window, text = '월', font = ('돋움체', 10))
    DayCombo = Combobox(Window, width = 2, height = 10, values = day)   
    DayCombo.configure(state = 'readonly')
    DayLabel = Label(Window, text = '일', font = ('돋움체', 10))

    YearCombo.place(x = 450, y = 150)
    YearLabel.place(x = 505, y = 150)
    MonthCombo.place(x = 525, y = 150)
    MonthLabel.place(x = 565, y = 150)
    DayCombo.place(x = 585, y = 150)
    DayLabel.place(x = 625, y= 150)

    PhoneLabel = Label(Window, text = '전화번호', font = ('돋움체', 10))  # 전화번호
    PhoneLabel.place(x = 380, y = 185)
    PhoneEnter1 = Entry(Window, width = 5)
    DashLabel1 = Label(Window, text = '-')
    PhoneEnter2 = Entry(Window, width = 6)
    DashLabel2 = Label(Window, text = '-')
    PhoneEnter3 = Entry(Window, width = 6)
    PhoneEnter1.place(x = 450, y = 185)
    DashLabel1.place(x = 495, y = 185)
    PhoneEnter2.place(x = 510, y = 185)
    DashLabel2.place(x = 564, y = 185)
    PhoneEnter3.place(x = 580, y = 185)

    MailLabel = Label(Window, text = '이메일', font = ('돋움체', 10))   # 이메일
    MailLabel.place(x = 395, y = 220)
    MailLabel2 = Label(Window, text = '@')
    MailLabel2.place(x = 535, y = 220)
    MailEnter = Entry(Window, width = 11)                                # 이메일 텍스트
    MailCombo = Combobox(Window, width = 8, height = 5, values = ['naver.com','gmail.com','daum.net'])
    MailCombo.configure(state = 'readonly')
    MailEnter.place(x = 450, y = 220)
    MailCombo.place(x = 550, y = 220)

    global pic
    pic = ''

    def SelectPic():             # 이미지 파일열기 함수
        filename = askopenfilename(parent = Window, filetypes = (('JPG 파일', '*jpg'),('GIF 파일','*gif'),('모든파일','*.*')))                       # [취소시 사진사라지는거]
        image = Image.open(filename)
        image = image.resize((170,200))
        photo = ImageTk.PhotoImage(image, master = Window)
        ImageButton.configure(image = photo)
        ImageButton.image = photo
        global pic
        pic = filename

    ImageButton = Button(Window, command = SelectPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

    def AddUser():  #회원 등록 누를 시
        global UserDf
        phone = PhoneEnter1.get() + '-'+PhoneEnter2.get() + '-' + PhoneEnter3.get()
        if '' in [NameEnter.get(), YearCombo.get(), MonthCombo.get(), DayCombo.get(), PhoneEnter1.get(),
        PhoneEnter2.get(), PhoneEnter3.get(), MailEnter.get(), MailCombo.get()]:
            messagebox.showerror('등록 오류', '올바른 정보를 입력하세요. \n 빈칸을 모두 채워주십시오.', master=Window)
        elif ((PhoneEnter1.get().isdigit() != True) or (PhoneEnter2.get().isdigit() != True) or (PhoneEnter3.get().isdigit() != True)):
            messagebox.showerror('입력오류', '전화번호에 숫자만 입력해 주세요', master = Window)
        elif (len(PhoneEnter1.get()) != 3 or len(PhoneEnter2.get()) != 4 or len(PhoneEnter3.get()) != 4):
            messagebox.showerror('입력오류', '전화번호 입력이 잘 못 되었습니다.', master = Window)
        elif (UserDf['USER_PHONE']==phone).any():
            messagebox.showerror('중복된 회원', '중복된 회원입니다. \n (오류 : 전화번호 중복)', master=Window)
        elif (int(YearCombo.get())%4 != 0 and int(MonthCombo.get()) == 2 and int(DayCombo.get()) > 28):
            messagebox.showerror('날짜 오류', '날짜가 형식에 맞지 않습니다.', master = Window)    
        elif (int(MonthCombo.get()) == 2 and int(DayCombo.get())>29) or ((int(MonthCombo.get()) == 4 or 
        int(MonthCombo.get()) == 6 or int(MonthCombo.get()) == 9 or int(MonthCombo.get())== 11) and int(DayCombo.get())>30):
            messagebox.showerror('날짜 오류', '날짜가 형식에 맞지 않습니다.', master = Window)
        
        else:
            AddUserDf = pd.DataFrame({'USER_NAME':[NameEnter.get()],        
         'USER_BIRTH':[YearCombo.get()+MonthCombo.get()+DayCombo.get()],
         'USER_PHONE':[phone],
         'USER_SEX':[PutSex],               #True : 남성 / False : 여성
         'USER_MAIL':[MailEnter.get()+'@'+MailCombo.get()],
         'USER_OUT':[' '],             #탈퇴일 디폴트 값 : 공백
         'USER_IN':[NowDay],        #등록일 디폴트 값 : 오늘 날짜
         'USER_RENT':[0],           #대여 디폴트 값 : 0
         'USER_PIC':[None]})            #사진 디폴트 값 : None
            if pic != '':
                AddUserDf['USER_PIC'] = [pic]
            UserDf = pd.concat([UserDf, AddUserDf])         #등록 정보를 기존 데이터프레임에 합치기
            UserDf.to_csv('UserList.csv',index=False,encoding='utf-8')  #csv파일에 저장
            messagebox.showinfo('등록 완료', '등록이 완료되었습니다.')  #등록 완료 메시지
            Window.destroy()

    #버튼
    OkButton = Button(Window, text = '등록', command=AddUser)      # 등록 버튼
    OkButton.place(x = 155, y = 290, width = 50)
    OutButton = Button(Window, text = '취소', command=Window.destroy)                       # 취소 버튼
    OutButton.place(x = 230, y = 290, width = 50)




    Window.mainloop()
