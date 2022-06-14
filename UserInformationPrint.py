from tkinter import *
from tkinter import messagebox
import math
from datetime import datetime, timedelta
import pandas as pd
from tkinter.filedialog import *

#유저
def UserInfowindow(PhoneNumber):

    UserDf = pd.read_csv(r'.\UserList.csv')
    RentDf = pd.read_csv('.\RentList.csv')
    BookDf = pd.read_csv('.\BookList.csv')
    
    Window = Tk()

    Window.title('회원 세부 정보')
    Window.geometry('700x450')
    Window.resizable(width = False, height = False)

    PN = PhoneNumber

    SomeDf = UserDf.loc[UserDf['USER_PHONE'].str.contains(PN)]              # 유저폰번호를 통해 해당 데이터프레임 가져옴
    for i in SomeDf.values:                                                 # 데이터프레임의 값을 각각 저장
        name, birth, phone, sex, mail, out, in1, rent, pic = i
    
    IsbnDf = RentDf.loc[RentDf['USER_PHONE'].str.contains(PN), ['BOOK_ISBN']]   # 대여목록출력 위해 isbn찾고 도서명,저자,출판사뽑기

# 텍스트

    NameLabel = Label(Window, text = '이름', font=('돋움체', 10))    # 이름
    NameLabel.place(x = 410, y = 80)
    NameEnter = Entry(Window, width = 25)                             # 이름 텍스트
    NameEnter.insert(0,name)                                              # 데이터프레임 이름 삽입
    NameEnter.place(x = 450, y = 80)

    SexLabel = Label(Window, text = '성별', font = ('돋움체', 10))     # 성별
    SexLabel.place(x = 410, y = 115)

    var = IntVar()                                                                      # 성별 라디오버튼
    SexRadioButton1 = Radiobutton(Window, text = '남성', variable = var, value = 1)
    SexRadioButton1.place(x= 450, y = 115)
    SexRadioButton2 = Radiobutton(Window, text = '여성', variable = var, value = 2)
    SexRadioButton2.place(x = 500, y = 115)
    if sex == True:
        SexRadioButton1.select()
    else:
        SexRadioButton2.select()

    BirthLabel = Label(Window, text = '생년월일', font = ('돋움체', 10))    # 생년월일
    BirthLabel.place(x = 380, y = 150)
    BirthEnter = Entry(Window, width = 25)                            # 생년월일 텍스트
    BirthEnter.insert(0,birth)                                               # 텍스트창에 생년월일 삽입
    BirthEnter.place(x = 450, y = 150)

    PhoneLabel = Label(Window, text = '전화번호', font = ('돋움체', 10))  # 전화번호
    PhoneLabel.place(x = 380, y = 185)
    PhoneEnter = Entry(Window, width = 25)                                # 전화번호 텍스트
    PhoneEnter.insert(0,phone)                                              # 텍스트창에 전화번호 삽입
    PhoneEnter.place(x = 450, y = 185)

    MailLabel = Label(Window, text = '이메일', font = ('돋움체', 10))   # 이메일
    MailLabel.place(x = 395, y = 220)
    MailEnter = Entry(Window, width = 25)                                # 이메일 텍스트
    MailEnter.insert(0,mail)                                                # 텍스트창에 이메일 삽입
    MailEnter.place(x = 450, y = 220)

    OutLabel = Label(Window, text = '탈퇴', font = ('돋움체', 10))     # 탈퇴
    OutLabel.place(x = 410, y = 255)
    OutEnter = Entry(Window, width = 25)                                # 탈퇴 텍스트
    OutEnter.place(x = 450, y = 255)
    try:
        if math.isnan(out) == True:                 # True = nan => 가입중 / False = 탈퇴일
            OutEnter.insert(0,'가입중')
    except:
        OutEnter.insert(0,out)
        
    # 대여목록 가져오는 코드
    ListDf = RentDf.loc[RentDf['USER_PHONE'].str.contains(PN), ['BOOK_ISBN']]

    RentLabel = Label(Window, text = '대여여부', font = ('돋움체', 10))   # 대여여부                                         [대여목록 출력해야함 > 맨위 IsbnDf 부분]
    RentLabel.place(x = 380, y = 290)
    RentEnter = Text(Window, width = 25, height = 1)                        # 대여목록
    RentEnter.insert(0.0,'')                                                     #                                              [rent.csv에서 isbn으로 책 제목,저자 출력]
    RentEnter.place(x = 450, y = 290)

# 버튼
    def SelectPic():                                                           # 이미지 파일열기 함수
        filename = askopenfilename(parent = Window, filetypes = (('GIF 파일','*gif'),('모든파일','*.*')))                       # [취소시 사진사라지는거]
        photo = PhotoImage(file = filename)
        ImageButton.configure(image = photo)
        ImageButton.image = photo
        UserDf.loc[UserDf['USER_PHONE'].str.contains(PN), ['USER_PIC']] = filename

    try:
        if math.isnan(pic):
            ImageButton = Button(Window, image = '', command = SelectPic)                          # 회원 이미지 추가버튼
    except(TypeError):
        try:
            photo = PhotoImage(file = pic)
            ImageButton = Button(Window, image = photo, command = SelectPic)
        except:
            ImageButton = Button(Window, text = '저장된 이미지가\n 삭제되었거나 없습니다.', command = SelectPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

    OkButton = Button(Window, text = '확인', command = Window.destroy)                            # 확인 버튼
    OkButton.place(x = 130, y = 290, width = 50)

    E_Name = NameEnter.get()
    E_Birth = BirthEnter.get()
    E_Phone = PhoneEnter.get()
    E_Mail = MailEnter.get()

    def EditUser():                                                                 # 수정버튼 누를시 실행 함수
        answer = messagebox.askquestion('수정', '수정하시겠습니까?')
        if answer == 'yes':
            if (PhoneEnter.get() != PN) and (PhoneEnter.get() == UserDf['USER_PHONE']).any():                             # 전화번호 중복확인
                messagebox.showerror('중복', '중복된 전화번호입니다.')
            else:
                if var.get() == 1:
                    sex = True
                else:
                    sex = False
                UserDf.loc[UserDf['USER_PHONE'].str.contains(PN), ['USER_NAME','USER_BIRTH','USER_PHONE','USER_SEX','USER_MAIL']] = (NameEnter.get(),BirthEnter.get(),PhoneEnter.get(),sex,MailEnter.get())
                UserDf.to_csv('UserList.csv', index=False, encoding = 'utf-8')
                messagebox.showinfo('수정완료', '수정되었습니다.')
                print(pic)
    

    EditButton = Button(Window, text = '수정', command = EditUser)      # 수정 버튼
    EditButton.place(x = 190, y = 290, width = 50)

    def OutUser():                                                                  # 탈퇴버튼 누를시 실행 함수
        try:
            if math.isnan(out) == True:
                if rent == False:
                    answer = messagebox.askquestion('탈퇴', '탈퇴 하시겠습니까?')                                 # 탈퇴 확인 메세지창
                    if answer == 'yes':
                        UserDf.loc[UserDf['USER_PHONE'].str.contains(PN),['USER_OUT']] = (datetime.today().strftime('%Y-%m-%d'))    # 확인시 데이터프레임에 탈퇴 날짜 저장
                        UserDf.to_csv('UserList.csv', index=False, encoding = 'utf-8')
                        messagebox.showinfo('탈퇴 완료', '탈퇴 되었습니다.\n 탈퇴정보가 바뀝니다.')
                        Window.destroy()
                    else:
                        messagebox.showinfo('탈퇴 취소', '탈퇴를 취소하였습니다.')
                else:
                    messagebox.showerror('오류', '도서를 대여 중인 회원입니다.')    
        except:
            messagebox.showerror('오류', '이미 탈퇴한 회원입니다.')

    OutButton = Button(Window, text = '탈퇴', command = OutUser)        # 탈퇴 버튼
    OutButton.place(x = 250, y = 290, width = 50)

    Window.mainloop()
