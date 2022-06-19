import pandas as pd

BookDf=pd.DataFrame({'BOOK_TITLE':['데미안','삼국유사','수레바퀴 아래서','언제나 밤인 세계'],
         'BOOK_ISBN':['9788937460449','9788937461668','9788937460500','9791170520634'],
         'BOOK_AUTHOR':['헤르만 헤세','일연','헤르만 헤세','하지은'],
         'BOOK_PUB':['민음사','민음사','민음사','황금가지'],
         'BOOK_PRICE':['8000','15000','8000','16800'],
         'BOOK_LINK':['https://A', 'https://B', 'https://C', 'https://D'],
         'BOOK_INFOR':['도서 정보1','도서 정보2','도서 정보3','도서 정보4'],
         'BOOK_RENT':['미대여','미대여','미대여','미대여'],
         'BOOK_PIC':[None, None, None, None]})

#도서 csv 생성
BookDf.to_csv('BookList.csv',index=False,encoding='utf-8-sig')        #csv파일 생성`