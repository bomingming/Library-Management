import pandas as pd
from datetime import datetime, timedelta

NowDay = datetime.today().strftime('%Y-%m-%d')  
ReturnDay = (datetime.today()+timedelta(days=14)).strftime('%Y-%m-%d')  #반납예정일

RentDf=pd.DataFrame({'BOOK_ISBN':[],
            'USER_PHONE':[],
            'RENT_DATE':[],
            'RENT_REDATE':[]})

#대여 csv 파일 생성
RentDf.to_csv('RentList.csv',index=False,encoding='utf-8')