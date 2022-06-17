import pandas as pd
from datetime import datetime, timedelta

NowDay = datetime.today().strftime('%Y-%m-%d')  
ReturnDay = (datetime.today()+timedelta(days=14)).strftime('%Y-%m-%d')  #반납예정일

RentDf=pd.DataFrame({'BOOK_ISBN':['9788937460449','9788937461668'],
            'USER_PHONE':['010-1234-5678','010-1234-5678'],
            'RENT_DATE':['2022-05-14','2022-05-11'],
            'RENT_REDATE':['2022-05-28','2022-05-19']})

#대여 csv 파일 생성
RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')