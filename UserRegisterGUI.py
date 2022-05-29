from tkinter import *
from tkinter.ttk import *

def UserRegister():       #등록 입력창
    RegisWindow = Tk()

    RegisWindow.title("회원 등록")          #새창 : 도서 등록
    RegisWindow.geometry("700x450")
    RegisWindow.resizable(width = FALSE, height = FALSE)

    NameEnter = Entry(RegisWindow, width = 25)     #이름 입력창
    NameEnter.place(x=450, y=80)
    SexEnter = Entry(RegisWindow, width = 25)      #성별 입력창
    Sex=IntVar()
    SexEnter1=Radiobutton(RegisWindow,text='남성',value=0,variable=Sex) #성별 입력
    SexEnter2=Radiobutton(RegisWindow,text='여성',value=1,variable=Sex)
    SexEnter1.pack(fill='both')
    SexEnter2.pack(fill='both')
    SexEnter1.place(x=450, y=115)
    SexEnter2.place(x=500,y=115)
    BirthEnter = Entry(RegisWindow, width = 25)    #생년월일 입력창
    BirthEnter.place(x=450, y=150)
    PhoneEnter = Entry(RegisWindow, width = 25)     #전화번호 입력창
    PhoneEnter.place(x=450, y=185)
    MailEnter = Entry(RegisWindow, width = 25)      #이메일 입력창
    MailEnter.place(x=450, y=220)
    

    NameLabel = Label(RegisWindow, text = "이름", font=("돋움체",10))
    NameLabel.place(x=390, y=80)
    SexLabel = Label(RegisWindow, text = "성별", font=("돋움체",10))
    SexLabel.place(x=390, y=115)
    BirthLabel = Label(RegisWindow, text = "생년월일", font=("돋움체",10))
    BirthLabel.place(x=390, y=150)
    PhoneLabel = Label(RegisWindow, text = "전화번호", font=("돋움체",10))
    PhoneLabel.place(x=390, y=185)
    MailLabel = Label(RegisWindow, text = "이메일", font=("돋움체",10))
    MailLabel.place(x=390, y=220)

    #등록 버튼
    RegisterBotton=Button(RegisWindow,text='등록',command=RegisWindow.destroy)
    RegisterBotton.place(x=240,y=300)

    #취소 버튼
    CancelBotton=Button(RegisWindow,text='취소',command=RegisWindow.destroy)
    CancelBotton.place(x=100,y=300)

    RegisWindow.mainloop()

UserRegister()
