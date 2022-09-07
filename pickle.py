# pickle 데이터를 파일형태로 저장하는 것

import pickle
#profile_file = open("profile.pickle","wb") #b는 바이너리 타입이라는 거임 pickle을 쓰기 위해서는 항상 정의해줘야댐 , 인코딩은 따로 안해줘도돼
#profile = {"이름":"박명수", "나이":30, "취미": ["축구","골프","코딩"]}
#print(profile)
#pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
#profile_file.close()

# 불러오고 변수에 저장을 해서 사용할 수있게하는 작업
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) #file의 정보를 profile에 불러오기
print(profile)
profile_file.close()