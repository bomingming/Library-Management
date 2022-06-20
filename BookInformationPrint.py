from tkinter import *
from tkinter import messagebox
import pandas as pd
import math
from tkinter.filedialog import *
from PIL import ImageTk
from PIL import Image

def BookInfowindow(SelectBook):
    BIWindow = Tk()

    BIWindow.title('도서 세부 정보')
    BIWindow.geometry('700x450')
    BIWindow.resizable(width = False, height = False)

    isbnnum = str(SelectBook)

    BookDf = pd.read_csv('.\BookList.csv')
    RentDf = pd.read_csv('.\RentList.csv')

    BookDf = BookDf.astype({'BOOK_ISBN' : 'str'})                               # str.contains 사용위해 str형으로 변경
    RentDf = RentDf.astype({'BOOK_ISBN' : 'str'})

    ValuesDf = BookDf.loc[BookDf['BOOK_ISBN'].str.contains(isbnnum)]            # isbnnum있는지 확인후 있으면 해당행 ValuesDf에 저장
    for i in ValuesDf.values:                                                   # ValuesDf의 값들을 각변수에 저장
        title,isbn,author,pub,price,link,infor,rent,pic = i

    # 텍스트

    TitleLabel = Label(BIWindow, text = '도서 명', font=('돋움체', 10))    # 도서명
    TitleLabel.place(x = 390, y = 80)
    TitleEnter = Entry(BIWindow, width = 25)                             # 도서명 텍스트
    TitleEnter.insert(0,title)
    TitleEnter.place(x = 450, y = 80)

    AuthorLabel = Label(BIWindow, text = '저자', font=('돋움체', 10))    # 저자
    AuthorLabel.place(x = 410, y = 115)
    AuthorEnter = Entry(BIWindow, width = 25)                             # 저자 텍스트
    AuthorEnter.insert(0,author)
    AuthorEnter.place(x = 450, y = 115)

    PubLabel = Label(BIWindow, text = '출판사', font = ('돋움체', 10))    # 출판사
    PubLabel.place(x = 395, y = 150)
    PubEnter = Entry(BIWindow, width = 25)                              # 출판사 텍스트
    PubEnter.insert(0,pub)
    PubEnter.place(x = 450, y = 150)

    IsbnLabel = Label(BIWindow, text = 'ISBN', font = ('돋움체', 10))      # ISBN
    IsbnLabel.place(x = 410, y = 185)
    IsbnEnter = Entry(BIWindow, width = 25)                                # ISBN 텍스트
    IsbnEnter.insert(0,isbn)
    IsbnEnter.place(x = 450, y = 185)

    PriceLabel = Label(BIWindow, text = '가격', font = ('돋움체', 10))       # 가격  
    PriceLabel.place(x = 410, y = 220)
    PriceEnter = Entry(BIWindow, width = 25)                                # 가격 텍스트
    PriceEnter.insert(0,price)
    PriceEnter.place(x = 450, y = 220)

    LinkLabel = Label(BIWindow, text = '링크', font = ('돋움체', 10))       # 링크
    LinkLabel.place(x = 410, y = 255)
    LinkEnter = Entry(BIWindow, width = 25)                                 # 링크 텍스트
    LinkEnter.insert(0,link)
    LinkEnter.place(x = 450, y = 255)

    RentLabel = Label(BIWindow, text = '대여여부', font = ('돋움체', 10))      # 대여여부
    RentLabel.place(x = 380, y = 290)
    RentEnter = Entry(BIWindow, width = 25)                                     # 대여여부 텍스트
    RentEnter.insert(0,rent)
    RentEnter.configure(state = 'readonly')
    RentEnter.place(x = 450, y = 290)

    InforLabel = Label(BIWindow, text = '도서설명', font = ('돋움체', 10))   # 도서설명
    InforLabel.place(x = 380, y = 325)
    InforEnter = Text(BIWindow, width = 25, height = 5)                        # 도서 설명 텍스트
    InforEnter.insert(0.0,infor)
    InforEnter.place(x = 450, y = 325)
    

    # 버튼
# 도서 이미지 버튼
    def SelectBookPic():
        filename = askopenfilename(parent = BIWindow, filetypes = (('JPG 파일','*jpg'),('GIF 파일','*gif'),('모든파일','*.*')))
        image = Image.open(filename)
        image = image.resize((170,200))
        if filename == '':
            photo = ImageTk.PhotoImage(image, master = BIWindow)
        else:
            photo = ImageTk.PhotoImage(image, master = BIWindow)
        ImageButton.configure(image = photo)
        ImageButton.image = photo
        BookDf.loc[BookDf['BOOK_ISBN'].str.contains(isbnnum), ['BOOK_PIC']] = filename

    try:
        if math.isnan(pic):
            ImageButton = Button(BIWindow, command = SelectBookPic)
    except(TypeError):
        try:
            image = Image.open(pic)
            image = image.resize((170,200))
            photo = ImageTk.PhotoImage(image, master = BIWindow)
            ImageButton = Button(BIWindow, image = photo, command = SelectBookPic)
        except:
            ImageButton = Button(BIWindow, command = SelectBookPic)
    ImageButton.place(x = 130, y = 80, width = 170, height = 200)

# 확인 버튼
    def OkBook():
        BIWindow.destroy()

    OkButton = Button(BIWindow, text = '확인', command = OkBook)
    OkButton.place(x = 130, y = 290, width = 50)

# 수정 버튼
    def EditBook():
        answer = messagebox.askquestion('수정', '수정하시겠습니까?', master = BIWindow)
        if answer == 'yes':
            #ISBN 문자열(숫자 외)등록 시 오류 처리        
            if ((IsbnEnter.get().isdigit())!=True) | ((PriceEnter.get().isdigit())!=True):
                messagebox.showerror('등록 오류', 'ISBN에 숫자를 입력해 주세요.', master=BIWindow)
            
            elif(IsbnEnter.get() != isbnnum) and (IsbnEnter.get() == BookDf['BOOK_ISBN']).any():              #[중복체크 수정할 필요있음]
                messagebox.showerror('중복', '중복된 ISBN 입니다.', master = BIWindow)

            elif '' in [TitleEnter.get(),IsbnEnter.get(),AuthorEnter.get(), PubEnter.get(),
                PriceEnter.get(), LinkEnter.get(), InforEnter.get(1.0, 'end-1c')]:
                messagebox.showerror('등록 오류', '올바른 정보를 입력하세요.', master=BIWindow)  #등록 오류 메시지(누락)
                
            else:
                BookDf.loc[BookDf['BOOK_ISBN'].str.contains(isbnnum),['BOOK_TITLE','BOOK_ISBN','BOOK_AUTHOR','BOOK_PUB','BOOK_PRICE','BOOK_LINK','BOOK_INFOR']] = (TitleEnter.get(),IsbnEnter.get(),AuthorEnter.get(),PubEnter.get(),PriceEnter.get(),LinkEnter.get(),InforEnter.get(0.0,'end-1c'))
                BookDf.to_csv('BookList.csv', index = False, encoding = 'utf-8')

                if (isbnnum == RentDf['BOOK_ISBN']).any():
                    RentDf.loc[RentDf['BOOK_ISBN'].str.contains(isbnnum), ['BOOK_ISBN']] = (IsbnEnter.get())
                    RentDf.to_csv('RentList.csv', index = False, encoding = 'utf-8')
                
                messagebox.showinfo('수정완료', '수정되었습니다.', master = BIWindow)
                BIWindow.destroy()

    EditButton = Button(BIWindow, text = '수정', command = EditBook)
    EditButton.place(x = 190, y = 290, width = 50)


# 삭제 버튼
    def DeleteBook():
        answer = messagebox.askquestion('삭제 확인','도서를 삭제하시겠습니까?', master = BIWindow)
        if answer == 'yes':
            DelIndex = BookDf[BookDf['BOOK_ISBN'] == isbnnum].index
            BookDelDf = BookDf.drop(DelIndex)
            BookDelDf.to_csv('BookList.csv', index=False, encoding = 'utf-8')
            messagebox.showinfo('삭제완료', '도서가 삭제되었습니다.', master = BIWindow)
            BIWindow.destroy()
            
    OutButton = Button(BIWindow, text = '삭제', command = DeleteBook)
    OutButton.place(x = 250, y = 290, width = 50)

    BIWindow.mainloop()
