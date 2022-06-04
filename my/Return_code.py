#반납
import tkinter
import pandas as pd

RERE = tkinter()

def ReturnBook():
    Userdf = pd.read_csv('UserList.csv')
    Bookdf = pd.read_csv('BookList.csv')

    #대여한 csv파일 열기
    f=open('BookList.csv','r',encoding='utf-8')

    RentBookIsbn = '9788937460449'
    if (RentBookIsbn in Bookdf["BOOK_RENT"]):
        INDEX = Bookdf[Bookdf["BOOK_ISBN"].str.contains(RentBookIsbn)].index
        Bookdf = Bookdf.drop(INDEX)
        Bookdf.to_csv('BOOK_RENT',index=True,encoding='utf-8')      
        Userdf.to_csv('USER_RENT',index=True,encoding='utf-8')

    #반납 검색 창 
def RETURN():
    RERE.title("반납")
    RERE.geometry("700X450")
    RERE.resizable(False, False)

    RERE.quit()     #위젯이 유지된채 mainloop()코드실행

   #메뉴생성
    menubar=tkinter.Menu(RERE)

    menu_1=tkinter.Menu(menubar, tearoff=False)     #tearoff 하위메뉴의 분리기능사용 유/무
    menubar.add_command(label="도서", menu=menu_1)  #상위메뉴1에 도서 추가
    menu_2=tkinter.Menu(menubar, tearoff=False)   
    menubar.add_command(label="회원", menu=menu_2)
    menu_3=tkinter.Menu(menubar, tearoff=False)   
    menubar.add_command(label="대여", menu=menu_3)
    menu_4=tkinter.Menu(menubar, tearoff=False)   
    menubar.add_command(label="반납", menu=menu_4)

    RERE.config(menu=menubar)
    
    RERE.mainloop()




