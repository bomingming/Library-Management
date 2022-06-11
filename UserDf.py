import pandas as pd
from datetime import datetime 

NowDay = datetime.today().strftime('%Y-%m-%d')  

UserDf=pd.DataFrame({'USER_NAME':['오영수','오정수','유민호','박영순','구병갑'],        
         'USER_BIRTH':['19980518','20000821','20100101','19990714','19901211'],
         'USER_PHONE':['010-1234-5678','010-1478-5236','010-8523-7413','010-9876-5432','010-9632-3542'],
         'USER_SEX':[True,True,False,False,True],               #True : 남성 / False : 여성
         'USER_MAIL':['younsu18@naver.com','int50821@google.com','minho01@google.com','sik0714@naver.com','gab12@google.com'],
         'USER_OUT':[None, None, None, None, None],             #탈퇴일 디폴트 값 : None
         'USER_IN':[NowDay,NowDay,NowDay,NowDay,NowDay],        #등록일 디폴트 값 : 오늘 날짜
         'USER_RENT':[False,False,False,False,False],           #대여 디폴트 값 : False
         'USER_PIC':[None, None, None, None, None]})            #사진 디폴트 값 : None

#회원 csv 파일 생성
UserDf.to_csv('UserList.csv',index=False,encoding='utf-8')