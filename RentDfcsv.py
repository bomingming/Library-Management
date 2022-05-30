import pandas as pd
from datetime import datetime, timedelta
import Book_code as Bc
import User_code as Uc

RentDay = datetime.today().strftime('%Y-%m-%d')
ReturnDay = (datetime.today()+timedelta(14)).strftime('%Y-%m-%d')

RentDf = pd.DataFrame({'BOOK_ISBN':['9788937460449','9788937461668'], 'USER_PHONE':['010-1234-5678','010-9876-5432'],
                        'RENT_DATE':[RentDay, RentDay], 'RENT_REDATE':[ReturnDay, ReturnDay]})


RentDf.to_csv('RentList.csv',index=False,encoding='utf-8') 