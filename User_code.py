import pandas as pd
import csv
from datetime import datetime 
from Rent_code import RentDf as RDf

NowDay = datetime.today().strftime('%Y-%m-%d')         #당일 날짜 표시

UserField=['USER_NAME','USER_BIRTH','USER_PHONE','USER_SEX','USER_MAIL',
                'USER_OUT','USER_RENT','USER_PIC']                          #필드 명 리스트

#데이터 프레임에 기본으로 있는 값들
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

#csv파일 열기
f=open('UserList.csv','r',encoding='utf-8')
Data=csv.reader(f) #data에 읽은 값 저장
header=next(Data) #csv파일의 1행 제거


#회원 검색
def UserSearch():                       
    Choice=input('이름, 전화번호 : ')    #검색 기준 선택(이름, 전화번호)
    if Choice=='이름':                  #이름으로 검색 시
        SearchIndex=0                   #이름 데이터 다루기
    elif Choice=='전화번호':            #전화번호로 검색 시
        SearchIndex=2                   #전화번호 데이터 다루기
        
    Name=input("{} 입력 : ".format(Choice))     #검색하고자 하는 값 입력
    print(UserField[0:6])                       #필드 명 출력
    for Row in Data:                            #data의 값
        if Name in Row[SearchIndex]:            #이름 데이터 목록에서 검색 값 검사
            print(Row[0:6])                     #해당하는 값 목록 출력
        elif Name == '':                        #아무것도 입력하지 않을 시
            print(Row[0:6])                     #해당하는 값 목록 출력


#회원 등록
def UserSave():
    global UserDf
    Name=input("이름 : ")           #이름 입력
    Phone=input("전화번호 : ")         #전화번호 입력
    Birth=input("생년월일 : ")         #생년월일 입력
    Sex=input("성별 : ")             #성별 입력
    if Sex=='남성':
        Sex=True
    elif Sex=='여성':
        Sex=False
    Mail=input("메일 : ")           #메일 입력
    Day=NowDay                      #오늘 날짜로 등록일 설정
    if '' in [Name,Phone,Birth,Sex,Mail]:        #입력값들로 리스트 생성 후 공백 있는 경우(정보값에 누락 O)
        print("올바른 값을 입력세요.")
    elif (UserDf['USER_PHONE']==Phone).any():               #등록한 정보가 기존 데이터 값과 중복될 경우
        print('중복된 회원입니다. 오류 : 전화번호 중복')
    else:
        AddUserDf = pd.DataFrame({'USER_NAME':[Name], 'USER_PHONE':[Phone],'USER_BIRTH':[Birth], 'USER_SEX':[Sex],'USER_MAIL':[Mail], 'USER_OUT':[None],
                            'USER_IN':[Day], 'USER_RENT':[False],'USER_PIC':[None]})       #입력값으로 새 데이터 프레임 생성
        UserDf = pd.concat([UserDf, AddUserDf])                                                 #기존 데이터 프레임에 합치기
        UserDf.to_csv('UserList.csv',index=False,encoding='utf-8')                            #csv 파일에 저장
        
    
#회원 수정
def UserAdit():
    ChangeName=input("변경할 회원 이름 ")                #수정할 회원 이름
    if (UserDf['USER_NAME']!=ChangeName).all():        #검색 값에 해당하는 데이터가 목록에 존재하지 않는 경우
        print('검색 결과가 없습니다.')
    else:
        Rent_Phone= UserDf.loc[UserDf['USER_NAME'].str.contains(ChangeName),('USER_PHONE')]                  ## 변경할 회원의 전화번호
        Name=input("이름 : ")
        Phone=input("번호 : ")
        if (UserDf['USER_PHONE']==Phone).any():               #등록한 정보가 기존 데이터 값과 중복될 경우
            print('중복된 회원입니다. 오류 : 전화번호 중복')
        else:
            UserDf.loc[UserDf['USER_NAME'].str.contains(ChangeName),('USER_NAME','USER_PHONE')]=(Name,Phone)      #기존 데이터 값에 수정 값 넣기
            UserDf.to_csv('UserList.csv',index=False,encoding='utf-8')                                            #csv 파일 추가

            if (RDf['USER_PHONE'] == Rent_Phone[0]).any():                                                        ## phone이 rent데이터프레임에 있을때
                RDf.loc[RDf['USER_PHONE'].str.contains(Rent_Phone[0]), ('USER_PHONE')] = Phone                    ## rent phone을 변경할 phone으로 바꿈

                RDf.to_csv('RentList.csv',index=False,encoding='utf-8')                                         ## 변경한 값으로csv 저장

#회원 탈퇴
def UserDel():
    Name=input('삭제할 회원 이름 ')          #삭제할 회원 이름
    if UserDf.loc[UserDf['USER_NAME'].str.contains(Name),('USER_RENT')].all()==True:        #해당 회원이 도서 대여 중일 경우
        print('도서 대여중 ')
    else:
        UserDf.loc[UserDf['USER_NAME'].str.contains(Name),'USER_OUT']=NowDay            #오늘 날짜로 탈퇴일 데이터 할당
        UserDf.to_csv('USERList.csv',index=False,encoding='utf-8')                      #csv 파일에 저장
 

#실행파일
UserSave()
#UserSearch()
#UserAdit()
#UserDel()
