from tkinter import *
from tkinter import messagebox

#유저
def UserInfowindow():
    UIWindow = Tk()

    UIWindow.title('회원 세부 정보')
    UIWindow.geometry('700x450')
    UIWindow.resizable(width = False, height = False)

    # 텍스트

    NameLabel = Label(UIWindow, text = '이름', font=('돋움체', 10))    # 이름
    NameLabel.place(x = 410, y = 80)
    NameEnter = Entry(UIWindow, width = 25)                             # 이름 텍스트
    NameEnter.insert(0,)                                              # [데이터프레임 이름 삽입]
    NameEnter.place(x = 450, y = 80)

    SexLabel = Label(UIWindow, text = '성별', font = ('돋움체', 10))     # 성별[라디오버튼 체크 표시? 어떻게?]
    SexLabel.place(x = 410, y = 115)

    var = IntVar()                                                                      # 성별 라디오버튼
    SexRadioButton1 = Radiobutton(UIWindow, text = '남성', variable = var, value = 1)
    SexRadioButton1.place(x= 450, y = 115)
    SexRadioButton2 = Radiobutton(UIWindow, text = '여성', variable = var, value = 2)
    SexRadioButton2.place(x = 500, y = 115)

    BirthLabel = Label(UIWindow, text = '생년월일', font = ('돋움체', 10))    # 생일
    BirthLabel.place(x = 380, y = 150)
    BirthEnter = Entry(UIWindow, width = 25)                            # 생일 텍스트
    BirthEnter.insert(0,)                                               # [데이터프레임 생일 삽입]
    BirthEnter.place(x = 450, y = 150)

    PhoneLabel = Label(UIWindow, text = '전화번호', font = ('돋움체', 10))  # 전화번호
    PhoneLabel.place(x = 380, y = 185)
    PhoneEnter = Entry(UIWindow, width = 25)                                # 전화번호 텍스트
    PhoneEnter.insert(0,)                                                   # [데이터프레임 전화번호 삽입]
    PhoneEnter.place(x = 450, y = 185)

    EmailLabel = Label(UIWindow, text = '이메일', font = ('돋움체', 10))   # 이메일
    EmailLabel.place(x = 395, y = 220)
    EmailEnter = Entry(UIWindow, width = 25)                                # 이메일 텍스트
    EmailEnter.insert(0,)                                                   # [데이터프레임 이메일 삽입]
    EmailEnter.place(x = 450, y = 220)

    OutLabel = Label(UIWindow, text = '탈퇴', font = ('돋움체', 10))     # 탈퇴
    OutLabel.place(x = 410, y = 255)
    OutEnter = Entry(UIWindow, width = 25)                                # 탈퇴 텍스트
    OutEnter.insert(0,)                                                   # [데이터프레임 탈퇴 삽입 => 탈퇴일 null = 탈퇴X]
    OutEnter.place(x = 450, y = 255)

    RentLabel = Label(UIWindow, text = '대여여부', font = ('돋움체', 10))   # 대여여부
    RentLabel.place(x = 380, y = 290)
    RentEnter = Entry(UIWindow, width = 25)                                  # 대여여부 텍스트
    RentEnter.insert(0,)                                                     # [rent.csv에서 isbn으로 책 제목,저자 출력]
    RentEnter.place(x = 450, y = 290)

    # 버튼
    ImageButton = Button(UIWindow, image = '')                          # 회원 이미지 추가버튼
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

    OkButton = Button(UIWindow, text = '확인')                            # 확인 버튼
    OkButton.place(x = 130, y = 290, width = 50)

    EditButton = Button(UIWindow, text = '수정')                          # 수정 버튼
    EditButton.place(x = 190, y = 290, width = 50)

    OutButton = Button(UIWindow, text = '탈퇴', command = OutUser)                           # 탈퇴 버튼
    OutButton.place(x = 250, y = 290, width = 50)
    

def EditInfo():       # 수정 후 수정 확인 메세지 창
    messagebox.showinfo('수정완료','수정이 완료되었습니다.')

def OverlapUserError():  # 수정 시 중복 오류 메세지 창
    messagebox.showerror('중복 오류', '중복된 회원입니다.\n (오류 : 전화번호 중복)')

def FormError():     # 수정 시 양식 오류 메세지 창
    messagebox.showerror('양식 오류', '올바른 양식을 입력하세요.')

def RentError():     # 탈퇴 시 대여중 오류 메세지 창
    messagebox.showerror('대여 오류', '도서를 대여 중인 회원입니다.')

def OutAsk():      # 탈퇴 시 탈퇴 확인 메세지 창
    answer = messagebox.askquestion('탈퇴','탈퇴 하시겠습니까?')
    if answer == 'yes':
        #[해당 데이터프레임에서 탈퇴여부에 date 삽입]
        messagebox.showinfo('탈퇴 완료', '탈퇴 되었습니다.')  # [위 문구 작성시 삭제]




'''
UserInfowindow()
EditInfo()
OverlapUserError()
FormError()
RentError()
OutAsk()
BookInfowindow()
OverlapBookError()
RentBookError()
DeleteBookInfo()
'''

