from tkinter import *
from tkinter import messagebox
import tkinter.ttk
import math
from datetime import datetime, timedelta
import pandas as pd
from tkinter.filedialog import *
import numpy as np

#유저
def UserInfowindow(PhoneNumber):

    UserDf = pd.read_csv(r'.\UserList.csv')
    RentDf = pd.read_csv('.\RentList.csv')
    BookDf = pd.read_csv('.\BookList.csv')
    
    UIWindow = Tk()

    UIWindow.title('회원 세부 정보')
    UIWindow.geometry('700x450')
##    UIWindow.resizable(width = False, height = False)

    PN = PhoneNumber

    SomeDf = UserDf.loc[UserDf['USER_PHONE'].str.contains(PN)]              # 유저폰번호를 통해 해당 데이터프레임 가져옴
    for i in SomeDf.values:                                                 # 데이터프레임의 값을 각각 저장
        name, birth, phone, sex, mail, out, in1, rent, pic = i
    mailid = mail.split('@')
    birth = str(birth)
    

# 텍스트

    NameLabel = Label(UIWindow, text = '이름', font=('돋움체', 10))    # 이름
    NameLabel.place(x = 410, y = 80)
    NameEnter = Entry(UIWindow, width = 25)                             # 이름 텍스트
    NameEnter.insert(0,name)                                              # 데이터프레임 이름 삽입
    NameEnter.place(x = 450, y = 80)

    SexLabel = Label(UIWindow, text = '성별', font = ('돋움체', 10))     # 성별
    SexLabel.place(x = 410, y = 115)

    sexvar = IntVar()                                                                      # 성별 라디오버튼
    SexRadioButton1 = Radiobutton(UIWindow, text = '남성', variable = sexvar, value = 0)
    SexRadioButton1.place(x= 450, y = 115)
    SexRadioButton2 = Radiobutton(UIWindow, text = '여성', variable = sexvar, value = 1)
    SexRadioButton2.place(x = 500, y = 115)
    if sex == True:
        SexRadioButton1.select()
    else:
        SexRadioButton2.select()


    year = [str(i) for i in range(1950, 2051)]
    month = [str(i).zfill(2) for i in range(1, 13)]
    day = [str(i).zfill(2) for i in range(1, 32)]
    

    BirthLabel = Label(UIWindow, text = '생년월일', font = ('돋움체', 10))                 # 생년월일
    BirthLabel.place(x = 380, y = 150)
    YearCombo = tkinter.ttk.Combobox(UIWindow, width = 4, height = 15, values = year)
    YearCombo.insert(0,birth[0:4])
    YearCombo.configure(state = 'readonly')
    YearLabel = Label(UIWindow, text = '년', font = ('돋움체', 10))
    MonthCombo = tkinter.ttk.Combobox(UIWindow, width = 2, height = 10, values = month)
    MonthCombo.insert(0,birth[4:6])
    MonthCombo.configure(state = 'readonly')
    MonthLabel = Label(UIWindow, text = '월', font = ('돋움체', 10))
    DayCombo = tkinter.ttk.Combobox(UIWindow, width = 2, height = 10, values = day)   
    DayCombo.insert(0,birth[6:8])
    DayCombo.configure(state = 'readonly')
    DayLabel = Label(UIWindow, text = '일', font = ('돋움체', 10))
    
    YearCombo.place(x = 450, y = 150)
    YearLabel.place(x = 505, y = 150)
    MonthCombo.place(x = 525, y = 150)
    MonthLabel.place(x = 565, y = 150)
    DayCombo.place(x = 585, y = 150)
    DayLabel.place(x = 625, y= 150)
    

    PhoneLabel = Label(UIWindow, text = '전화번호', font = ('돋움체', 10))  # 전화번호
    PhoneLabel.place(x = 380, y = 185)
    PhoneEnter1 = Entry(UIWindow, width = 5)
    PhoneEnter1.insert(0,phone[0:3])
    DashLabel1 = Label(UIWindow, text = '-')
    PhoneEnter2 = Entry(UIWindow, width = 6)
    PhoneEnter2.insert(0,phone[4:8])
    DashLabel2 = Label(UIWindow, text = '-')
    PhoneEnter3 = Entry(UIWindow, width = 6)
    PhoneEnter3.insert(0,phone[9:13])
    PhoneEnter1.place(x = 450, y = 185)
    DashLabel1.place(x = 495, y = 185)
    PhoneEnter2.place(x = 510, y = 185)
    DashLabel2.place(x = 564, y = 185)
    PhoneEnter3.place(x = 580, y = 185)
    
    MailLabel = Label(UIWindow, text = '이메일', font = ('돋움체', 10))   # 이메일
    MailLabel.place(x = 395, y = 220)
    MailLabel2 = Label(UIWindow, text = '@')
    MailLabel2.place(x = 530, y = 220)
    MailEnter = Entry(UIWindow, width = 11)                                # 이메일 텍스트
    MailCombo = tkinter.ttk.Combobox(UIWindow, width = 8, height = 5, values = ['naver.com','gmail.com','daum.net'])
    MailCombo.configure(state = 'readonly')
    MailEnter.insert(0,mailid[0])                                                # 텍스트창에 이메일 삽입
    MailCombo.set(mailid[1])
    MailEnter.place(x = 450, y = 220)
    MailCombo.place(x = 550, y = 220)

    OutLabel = Label(UIWindow, text = '탈퇴', font = ('돋움체', 10))     # 탈퇴
    OutLabel.place(x = 410, y = 255)
    OutEnter = Entry(UIWindow, width = 25)                                # 탈퇴 텍스트
    OutEnter.place(x = 450, y = 255)
    try:
        if math.isnan(out) == True:                 # True = nan => 가입중 / False = 탈퇴일
            OutEnter.insert(0,'가입중')
    except:
        OutEnter.insert(0,out)
        

#대여목록
    RentTreeview = tkinter.ttk.Treeview(UIWindow, height = 5)
    RentTreeview.column('#0', width = 250, anchor = 'w')
    RentTreeview.heading('#0', text = '대여중인 도서', anchor = 'center')
    RentTreeview.place(x = 380, y = 290)

    ListDf = RentDf.loc[RentDf['USER_PHONE'].str.contains(PN)]
    a = ListDf['BOOK_ISBN'].tolist()
    
    BookDf = BookDf.astype({'BOOK_ISBN' : 'str'})
    c = []
    for i in a:
        i = str(i)
        b = (BookDf.loc[BookDf['BOOK_ISBN'].str.contains(i), ['BOOK_TITLE']])
        b = b.values
        b = np.array(b).flatten().tolist()
        RentTreeview.insert('','end',text = b)        

        
    c = np.array(c).flatten().tolist()
    

# 버튼
    def SelectPic():                                                           # 이미지 파일열기 함수
        filename = askopenfilename(parent = UIWindow, filetypes = (('GIF 파일','*gif'),('모든파일','*.*')))
        if filename == '':
            photo = PhotoImage(file = pic, master = UIWindow)
        else:
            photo = PhotoImage(file = filename, master = UIWindow)
        ImageButton.configure(image = photo)
        ImageButton.image = photo
        UserDf.loc[UserDf['USER_PHONE'].str.contains(PN), ['USER_PIC']] = filename

    try:
        if math.isnan(pic):
            ImageButton = Button(UIWindow, image = '', command = SelectPic)                          # 회원 이미지 추가버튼
    except(TypeError):
        try:
            photo = PhotoImage(file = pic, master = UIWindow)
            ImageButton = Button(UIWindow, image = photo, command = SelectPic)
        except:
            ImageButton = Button(UIWindow, text = '저장된 이미지가\n 삭제되었거나 없습니다.', command = SelectPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)


    def OkUser():
        UIWindow.destroy()

    OkButton = Button(UIWindow, text = '확인', command = OkUser)                            # 확인 버튼
    OkButton.place(x = 130, y = 290, width = 50)


    def EditUser():                                                                 # 수정버튼 누를시 실행 함수
        Year = int(YearCombo.get())
        Month = int(MonthCombo.get())
        Day = int(DayCombo.get())
        phone = PhoneEnter1.get()+'-'+PhoneEnter2.get()+'-'+PhoneEnter3.get()
        answer = messagebox.askquestion('수정', '수정하시겠습니까?', master = UIWindow)
        if answer == 'yes':
            if (phone != PN) and (phone == UserDf['USER_PHONE']).any():                             # 전화번호 중복확인
                messagebox.showerror('중복', '중복된 전화번호입니다.', master = UIWindow)
            else:
                if (Year%4 != 0 and Month == 2 and Day > 28):
                    messagebox.showerror('날짜 오류', '날짜가 형식에 맞지 않습니다.', master = UIWindow)
                
                elif (Month == 2 and Day>29) or ((Month == 4 or Month == 6 or Month == 9 or Month == 11) and Day>30):
                    messagebox.showerror('날짜 오류', '날짜가 형식에 맞지 않습니다.', master = UIWindow)
                else:
                    if sexvar.get() == 0:
                        sex = True
                    else:
                        sex = False
                    mail = MailEnter.get()+'@'+MailCombo.get()
                    
                    birth = YearCombo.get()+MonthCombo.get()+DayCombo.get()
                    print(phone)

                    UserDf.loc[UserDf['USER_PHONE'].str.contains(PN), ['USER_NAME','USER_BIRTH','USER_PHONE','USER_SEX','USER_MAIL']] = (NameEnter.get(),birth,phone,sex,mail)
                    UserDf.to_csv('UserList.csv', index=False, encoding = 'utf-8')
                    
                    messagebox.showinfo('수정완료', '수정되었습니다.', master = UIWindow)
                    UIWindow.destroy()
    

    EditButton = Button(UIWindow, text = '수정', command = EditUser)      # 수정 버튼
    EditButton.place(x = 190, y = 290, width = 50)

    def OutUser():                                                                  # 탈퇴버튼 누를시 실행 함수
        try:
            if math.isnan(out) == True:
                if rent == False:
                    answer = messagebox.askquestion('탈퇴', '탈퇴 하시겠습니까?', master = UIWindow)                                 # 탈퇴 확인 메세지창
                    if answer == 'yes':
                        UserDf.loc[UserDf['USER_PHONE'].str.contains(PN),['USER_OUT']] = (datetime.today().strftime('%Y-%m-%d'))    # 확인시 데이터프레임에 탈퇴 날짜 저장
                        UserDf.to_csv('UserList.csv', index=False, encoding = 'utf-8')
                        messagebox.showinfo('탈퇴 완료', '탈퇴 되었습니다.', master = UIWindow)
                        UIWindow.destroy()
                    else:
                        messagebox.showinfo('탈퇴 취소', '탈퇴를 취소하였습니다.', master = UIWindow)
                else:
                    messagebox.showerror('오류', '도서를 대여 중인 회원입니다.', master = UIWindow)    
        except:
            messagebox.showerror('오류', '이미 탈퇴한 회원입니다.', master = UIWindow)

    OutButton = Button(UIWindow, text = '탈퇴', command = OutUser)        # 탈퇴 버튼
    OutButton.place(x = 250, y = 290, width = 50)

    UIWindow.mainloop()
