from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd
from tkinter.filedialog import *
from PIL import ImageTk
from PIL import Image

BookDf = pd.read_csv('BookList.csv')

#도서 세부 정보 함수
def BookInfowindow():

    Window = Tk()
    Window.title('도서 세부 정보')
    Window.geometry('700x450')
    Window.resizable(width = False, height = False)

    # 텍스트
    TitleLabel = Label(Window, text = '도서 명', font=('돋움체', 10))    # 도서명
    TitleLabel.place(x = 390, y = 80)
    TitleEnter = Entry(Window, width = 25)    
    TitleEnter.place(x = 450, y = 80)

    AuthorLabel = Label(Window, text = '저자', font=('돋움체', 10))    # 저자
    AuthorLabel.place(x = 410, y = 115)
    AuthorEnter = Entry(Window, width = 25)                             # 저자 텍스트
    AuthorEnter.place(x = 450, y = 115)


    PublishLabel = Label(Window, text = '출판사', font = ('돋움체', 10))    # 출판사
    PublishLabel.place(x = 395, y = 150)
    PublishEnter = Entry(Window, width = 25)                              # 출판사 텍스트
    PublishEnter.place(x = 450, y = 150)

    IsbnLabel = Label(Window, text = 'ISBN', font = ('돋움체', 10))      # ISBN
    IsbnLabel.place(x = 410, y = 185)
    IsbnEnter = Entry(Window, width = 25)                                # ISBN 텍스트
    IsbnEnter.place(x = 450, y = 185)

    PriceLabel = Label(Window, text = '가격', font = ('돋움체', 10))       # 가격  
    PriceLabel.place(x = 410, y = 220)
    PriceEnter = Entry(Window, width = 25)                                # 가격 텍스트
    PriceEnter.place(x = 450, y = 220)

    LinkLabel = Label(Window, text = '링크', font = ('돋움체', 10))       # 링크
    LinkLabel.place(x = 410, y = 255)
    LinkEnter = Entry(Window, width = 25)                                 # 링크 텍스트
    LinkEnter.place(x = 450, y = 255)

    BookInfomationLabel = Label(Window, text = '도서설명', font = ('돋움체', 10))   # 도서설명
    BookInfomationLabel.place(x = 380, y = 290)
    BookInfomationEnter = Text(Window, width = 25, height = 5)                        # 도서 설명 텍스트

    BookInfomationEnter.place(x = 450, y = 290)


    def SelectPic():             # 이미지 파일열기 함수
        filename = askopenfilename(parent = Window, filetypes = (('JPG 파일','*jpg'),('GIF 파일','*gif'),('모든파일','*.*')))
        image = Image.open(filename)
        image = image.resize((170,200))
        photo = ImageTk.PhotoImage(image, master = Window)
        ImageButton.configure(image = photo)
        ImageButton.image = photo

    ImageButton = Button(Window, text = '저장된 이미지가\n삭제되었거나 없습니다.', command = SelectPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)
    

    def AddBook():  #도서 등록 버튼 누를 시
        global BookDf
        if (BookDf['BOOK_ISBN']==IsbnEnter.get()).any():
            messagebox.showerror('중복된 도서', '중복된 도서입니다. \n (오류 : ISBN 중복)', master=Window) #등록 오류 메시지(중복)
        elif '' in [TitleEnter.get(),IsbnEnter.get(),AuthorEnter.get(), PublishEnter.get(),
            PriceEnter.get(), LinkEnter.get(), BookInfomationEnter.get(1.0, 'end-1c')]:
            messagebox.showerror('등록 오류', '올바른 정보를 입력하세요.', master=Window)  #등록 오류 메시지(누락)
            
        #ISBN 문자열(숫자 외)등록 시 오류 처리        
        elif ((IsbnEnter.get().isdigit())!=True) | ((PriceEnter.get().isdigit())!=True):
            messagebox.showerror('등록 오류', 'ISBN 또는 가격을 숫자로 입력하세요.', master=Window) #등록 오류 메시지(잘못된 입력)
        elif (len(IsbnEnter.get()) != 13):
            messagebox.showerror('등록 오류', '13자리 ISBN를 입력하세요.', master=Window) #등록 오류 메시지(잘못된 입력)
        else:
            AddDf = pd.DataFrame({'BOOK_TITLE':[TitleEnter.get()],
                'BOOK_ISBN':[IsbnEnter.get()],
                'BOOK_AUTHOR':[AuthorEnter.get()],
                'BOOK_PUB':[PublishEnter.get()],
                'BOOK_PRICE':[PriceEnter.get()],
                'BOOK_LINK':[LinkEnter.get()],
                'BOOK_INFOR':[BookInfomationEnter.get(1.0, 'end-1c')],     #임의로 설정한 저장값
                'BOOK_PIC':[None]})
            BookDf = pd.concat([BookDf, AddDf])         #등록 정보를 기존 데이터프레임에 합치기

            BookDf.to_csv('BookList.csv',index=False,encoding='utf-8')  #csv파일에 저장

            messagebox.showinfo('등록 완료', '등록이 완료되었습니다.')  #등록 완료 메시지
            Window.destroy()    #도서 등록 후 도서 등록 창 제거

    OkButton = Button(Window, text = '등록', command=AddBook)      # 등록 버튼
    OkButton.place(x = 155, y = 290, width = 50)

    OutButton = Button(Window, text = '취소',command=Window.destroy)    # 취소 버튼
    OutButton.place(x = 230, y = 290, width = 50)
    
    Window.mainloop()
