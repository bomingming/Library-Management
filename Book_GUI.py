from tkinter import *
from tkinter.ttk import *


Window = Tk()


def Default():      #기본 화면 함수
    DefaultLabel = Label(Window, text = "도서 관리 프로그램", font=("돋움체",25))      #대표 텍스트
    DefaultLabel.place(x=230, y=190)                                                  #위젯 위치
    SubLabel = Label(Window, text = "원하는 메뉴를 선택하세요.", font=("돋움체", 15))   #부제 텍스트
    SubLabel.place(x=255, y=237)                                                      #위젯 위치


def SearchBar():         #검색창 함수
    Search = Entry(Window, width=55)      #검색창 생성
    Search.place(x=230, y=200)  #검색창 위치 지정


def BookSearchType():  #검색 기준 콤보박스 함수
    Combo = Combobox(Window, width=10)
    Combo['values']=("도서 명", "저자", "출판사")   #검색 기준
    Combo.current(0)                               #디폴트값 : 첫번째 값
    Combo.grid(row=1, column=1)                    #위젯 순서
    Combo.place(x=130,y=200)                       #위젯 위치


def UserSearchType():  #검색 기준 콤보박스 함수
    Combo = Combobox(Window, width=10)
    Combo['values']=("회원 이름", "전화번호")   #검색 기준
    Combo.current(0)                               #디폴트값 : 첫번째 값
    Combo.grid(row=1, column=1)                    #위젯 순서
    Combo.place(x=130,y=200)


def RegisButton():     #등록 버튼 함수
    RegisButton = Button(Window, text = "도서 등록")
    RegisButton.grid(row=0, column=0)           #위젯 순서
    RegisButton.place(x=230, y=167)             #위젯 위치


def SearchList():       #검색 목록 함수(보민)
    Search = Entry(Window, width=55)      #검색창 생성
    Search.place(x=230, y=80)  #검색창 위치 지정

    Combo = Combobox(Window, width=10)
    Combo['values']=("도서 명", "저자", "출판사")   #검색 기준
    Combo.current(0)                               #디폴트값 : 첫번째 값
    Combo.pack()
    Combo.place(x=130,y=80)

    SearchList = Text(Window, width = 70, height = 17)       #도서 설명 입력창
    SearchList.place(x=130, y=130)


def CheckButton():      #선택 버튼 함수
    CheckButton = Button(Window, text = "선택")
    CheckButton.grid(row=0, column=0)
    CheckButton.place(x=535, y=365) 



def RegisEnter():       #등록 입력창
    RegisWindow = Tk()

    RegisWindow.title("도서 등록")          #새창 : 도서 등록
    RegisWindow.geometry("700x450")
    RegisWindow.resizable(width = FALSE, height = FALSE)

    TitleEnter = Entry(RegisWindow, width = 25)                     #도서 명 입력창
    TitleEnter.place(x=450, y=80)
    AuthorEnter = Entry(RegisWindow, width = 25)                    #저자 입력창
    AuthorEnter.place(x=450, y=115)
    PubEnter = Entry(RegisWindow, width = 25)                       #출판사 입력창
    PubEnter.place(x=450, y=150)
    IsbnEnter = Entry(RegisWindow, width = 25)                      #ISBN 입력창
    IsbnEnter.place(x=450, y=185)
    PriceEnter = Entry(RegisWindow, width = 25)      #가격 입력창
    PriceEnter.place(x=450, y=220)
    LinkEnter = Entry(RegisWindow, width = 25)       #링크 입력창
    LinkEnter.place(x=450, y=255)
    InforEnter = Text(RegisWindow, width = 25, height = 5)       #도서 설명 입력창
    InforEnter.place(x=450, y=290)

    TitleLabel = Label(RegisWindow, text = "도서 명", font=("돋움체",10))
    TitleLabel.place(x=390, y=80)
    AuthorLabel = Label(RegisWindow, text = "저자", font=("돋움체",10))
    AuthorLabel.place(x=410, y=115)
    PubLabel = Label(RegisWindow, text = "출판사", font=("돋움체",10))
    PubLabel.place(x=400, y=150)
    IsbnLabel = Label(RegisWindow, text = "ISBN", font=("돋움체",10))
    IsbnLabel.place(x=410, y=185)
    PriceLabel = Label(RegisWindow, text = "가격", font=("돋움체",10))
    PriceLabel.place(x=410, y=220)
    LinkLabel = Label(RegisWindow, text = "링크", font=("돋움체",10))
    LinkLabel.place(x=410, y=255)
    InforLabel = Label(RegisWindow, text = "도서 설명", font=("돋움체",10))
    InforLabel.place(x=375, y=290)


#도서 세부 정보 함수
def BookInfowindow():
    BIWindow = Tk()

    BIWindow.title('도서 세부 정보')
    BIWindow.geometry('700x450')
    BIWindow.resizable(width = False, height = False)

    # 텍스트

    TitleLabel = Label(BIWindow, text = '도서 명', font=('돋움체', 10))    # 도서명
    TitleLabel.place(x = 390, y = 80)
    TitleEnter = Entry(BIWindow, width = 25)                             # 도서명 텍스트
    TitleEnter.place(x = 450, y = 80)

    AuthorLabel = Label(BIWindow, text = '저자', font=('돋움체', 10))    # 저자
    AuthorLabel.place(x = 410, y = 115)
    AuthorEnter = Entry(BIWindow, width = 25)                             # 저자 텍스트
    AuthorEnter.place(x = 450, y = 115)


    PublishLabel = Label(BIWindow, text = '출판사', font = ('돋움체', 10))    # 출판사
    PublishLabel.place(x = 395, y = 150)
    PublishEnter = Entry(BIWindow, width = 25)                              # 출판사 텍스트
    PublishEnter.place(x = 450, y = 150)

    IsbnLabel = Label(BIWindow, text = 'ISBN', font = ('돋움체', 10))      # ISBN
    IsbnLabel.place(x = 410, y = 185)
    IsbnEnter = Entry(BIWindow, width = 25)                                # ISBN 텍스트
    IsbnEnter.place(x = 450, y = 185)

    PriceLabel = Label(BIWindow, text = '가격', font = ('돋움체', 10))       # 가격  
    PriceLabel.place(x = 410, y = 220)
    PriceEnter = Entry(BIWindow, width = 25)                                # 가격 텍스트
    PriceEnter.place(x = 450, y = 220)

    LinkLabel = Label(BIWindow, text = '링크', font = ('돋움체', 10))       # 링크
    LinkLabel.place(x = 410, y = 255)
    LinkEntry = Entry(BIWindow, width = 25)                                 # 링크 텍스트
    LinkEntry.place(x = 450, y = 255)

    RentLabel = Label(BIWindow, text = '대여여부', font = ('돋움체', 10))      # 대여여부
    RentLabel.place(x = 380, y = 290)
    RentEnter = Entry(BIWindow, width = 25)                                     # 대여여부 텍스트
    RentEnter.place(x = 450, y = 290)

    BookInfomationLabel = Label(BIWindow, text = '도서설명', font = ('돋움체', 10))   # 도서설명
    BookInfomationLabel.place(x = 380, y = 325)
    BookInfomationEnter = Text(BIWindow, width = 25, height = 5)                        # 도서 설명 텍스트
    BookInfomationEnter.place(x = 450, y = 325)
    

    # 버튼
    ImageButton = Button(BIWindow, image = '')                          # 도서 이미지 추가버튼
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

    OkButton = Button(BIWindow, text = '확인')                            # 확인 버튼
    OkButton.place(x = 130, y = 290, width = 50)

    EditButton = Button(BIWindow, text = '수정')                          # 수정 버튼
    EditButton.place(x = 190, y = 290, width = 50)

    OutButton = Button(BIWindow, text = '삭제')                           # 삭제 버튼
    OutButton.place(x = 250, y = 290, width = 50)
    

'''
def OverlapBookError():         # ISBN이 동일하게 수정시
    messagebox.showerror('중복된 도서', '중복된 도서입니다. \n (오류 : ISBN 중복)')

def RentBookError():            # 대여중 도서 삭제시
    messagebox.showerror('대여 중', '대여 중인 도서입니다.')

def DeleteBookInfo():
    messagebox.askquestion('삭제', '삭제 하시겠습니까?')
'''




Window.title("도서 관리 프로그램")      #프로그램 이름
Window.geometry("800x500")             #창 크기
Window.resizable(width = FALSE, height = FALSE)     #창 고정

MainMenu = Menu(Window)
Window.config(menu = MainMenu)

fileMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "도서", menu = fileMenu)
MainMenu.add_cascade(label = "회원", menu = fileMenu)
MainMenu.add_cascade(label = "대여", menu = fileMenu)
MainMenu.add_cascade(label = "반납", menu = fileMenu)


'''
Default()

SearchBar()
BookSearchType()
RegisButton()

RegisEnter()

UserSearchType()
SearchList()
CheckButton()

'''

BookInfowindow()

#RegisEnter()
Window.mainloop()