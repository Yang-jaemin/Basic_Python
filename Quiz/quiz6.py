#quiz 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중: 각 개인의 키에 적당한 체중

#(성별별 공식)
#남자 : 키(m) x 키(m) x 22
#여자 : 키(m) x 키(m) x 21

#조건1: 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 푯

#(출력 예제)
# 키 175cm 남자의 표준체중은 67.38입니다.

def std_weight(height,gender):
     if gender == "남자":
        std = ((0.01*height)**2) * 22
     elif gender == "여자":
        std = ((0.01*height)**2) * 21
     return std
 

height = int(input("키(cm)를 입력하세요: "))
gender = input("성별을 입력하세요: ")
std = round(std_weight(height,gender),2) #round 소수점 조절가능 round(x,2)
print("키{0}cm {1}의 표준체중은 {2}입니다. ".format(height,gender,std))