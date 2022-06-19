from tkinter import *
from tkinter.ttk import *
import pandas as pd
from tkinter import messagebox
from tkinter.filedialog import *
import RentUserSearch

#도서 세부 정보 함수
def BookInfowindow(SelectBook):

    BookDf = pd.read_csv('.\BookList.csv')

    Window = Tk()
    Window.title('도서 세부 정보')
    Window.geometry('700x450')
    Window.resizable(width = False, height = False)

    for i in BookDf.index:
        if BookDf.loc[i,'BOOK_ISBN']==SelectBook:
            OutputBook=BookDf.loc[i]
    # 텍스트

    TitleLabel = Label(Window, text = '도서 명', font=('돋움체', 10))    # 도서명
    TitleLabel.place(x = 390, y = 80)
    TitleEnter = Entry(Window, width = 25)
    TitleEnter.place(x = 450, y = 80)
    TitleEnter.insert(0,OutputBook[0])
    TitleEnter.configure(state = 'readonly')

    AuthorLabel = Label(Window, text = '저자', font=('돋움체', 10))    # 저자
    AuthorLabel.place(x = 410, y = 115)
    AuthorEnter = Entry(Window, width = 25)        # 저자 텍스트
    AuthorEnter.place(x = 450, y = 115)
    AuthorEnter.insert(0,OutputBook[2])
    AuthorEnter.configure(state = 'readonly')

    PublishLabel = Label(Window, text = '출판사', font = ('돋움체', 10))    # 출판사
    PublishLabel.place(x = 395, y = 150)
    PublishEnter = Entry(Window, width = 25)            # 출판사 텍스트
    PublishEnter.place(x = 450, y = 150)
    PublishEnter.insert(0,OutputBook[3])
    PublishEnter.configure(state = 'readonly')

    IsbnLabel = Label(Window, text = 'ISBN', font = ('돋움체', 10))      # ISBN
    IsbnLabel.place(x = 410, y = 185)
    IsbnEnter = Entry(Window, width = 25)            # ISBN 텍스트
    IsbnEnter.place(x = 450, y = 185)
    IsbnEnter.insert(0,OutputBook[2])
    IsbnEnter.configure(state = 'readonly')

    PriceLabel = Label(Window, text = '가격', font = ('돋움체', 10))       # 가격  
    PriceLabel.place(x = 410, y = 220)
    PriceEnter = Entry(Window, width = 25)             # 가격 텍스트
    PriceEnter.place(x = 450, y = 220)
    PriceEnter.insert(0,OutputBook[4])
    PriceEnter.configure(state = 'readonly')

    LinkLabel = Label(Window, text = '링크', font = ('돋움체', 10))       # 링크
    LinkLabel.place(x = 410, y = 255)
    LinkEnter = Entry(Window, width = 25)             # 링크 텍스트
    LinkEnter.place(x = 450, y = 255)
    LinkEnter.insert(0,OutputBook[5])
    LinkEnter.configure(state = 'readonly')


    BookInfomationLabel = Label(Window, text = '도서설명', font = ('돋움체', 10))   # 도서설명
    BookInfomationLabel.place(x = 380, y = 325)
    BookInfomationEnter = Text(Window, width = 25, height = 5)  # 도서 설명 텍스트
    BookInfomationEnter.insert(END,OutputBook[6])
    BookInfomationEnter.configure(state='disabled')

    BookInfomationEnter.place(x = 450, y = 325)

    def SelectPic():             # 이미지 파일열기 함수
        filename = askopenfilename(parent = Window, filetypes = (('GIF 파일','*gif'),('모든파일','*.*')))                       # [취소시 사진사라지는거]
        photo = PhotoImage(file = filename)
        ImageButton.configure(image = photo)
        ImageButton.image = photo

    ImageButton = Button(Window, text = '저장된 이미지가\n삭제되었거나 없습니다.', command = SelectPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)


    def Rent():  #대여 버튼 (수정 필요)
        global BookDf
        if (BookDf['BOOK_ISBN']==IsbnEnter.get()).any():
            messagebox.showerror('중복된 도서', '중복된 도서입니다. \n (오류 : ISBN 중복)') #등록 오류 메시지(중복)
        elif '' in [TitleEnter.get(),IsbnEnter.get(),AuthorEnter.get(), 
            AuthorEnter.get(), PriceEnter.get(), LinkEnter.get(),
            BookInfomationEnter.get(1.0, 50.50)]:
            messagebox.showerror('등록 오류', '올바른 정보를 입력하세요.')  #등록 오류 메시지(누락)

        else:
            BookDf.loc[BookDf[IsbnEnter.get()]]=[TitleEnter.get(),AuthorEnter.get(),PublishEnter.get(),
            IsbnEnter.get(),PriceEnter.get(),LinkEnter.get(),BookInfomationEnter.get(1.0, 50.50)]

            BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')  #csv파일에 저장

            messagebox.showinfo('수정 완료', '수정이 완료되었습니다.')  #등록 완료 메시지
            Window.destroy

    def Borrower():     #대여자 버튼
        global RentDf
        RentUserSearch.SearchWindow(SelectBook)
        #Window.destroy()    #대여 후 대여자 목록 창 제거


    OkButton = Button(Window, text = '대여', command=Rent)    # 대여 버튼
    OkButton.place(x = 130, y = 290, width = 50)

    OkButton = Button(Window, text = '대여자', command=Borrower)            # 대여자 버튼
    OkButton.place(x = 190, y = 290, width = 50)

    OutButton = Button(Window, text = '취소',command=Window.destroy)    # 취소 버튼
    OutButton.place(x = 250, y = 290, width = 50)

    Window.mainloop()