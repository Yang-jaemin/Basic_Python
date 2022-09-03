print(abs(-5)) # 의 절댓값 
print(pow(4,2)) # a의 b승 // 4^2 16
print(max(5,12)) #a b중 최댓값 // 12
print(min(4,12)) #a b중 최솟값 //4
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5 반올림

#수학 라이브러리 함수 사용

from math import * #나중에 배움
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 루트 a 4

#랜덤 함수

from random import *
print(random())
print(random()) # 0.0 이상 ~1.0 미만의 난수
print(random())

print(random() * 10) #0.0이상 ~ 10.0 미만 난수
#소수점이 싫다면?
print(int(random()*10))
print(int(random()*10))
print(int(random()*10)+1) #1부터 10이하의 난수

print(int(random()*45)+1) #1부터 45이하의 난수값 생성
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1) #로또 난수 ㅇㅇ
#좀더 쉽게 randrange
print(randrange(1,46)) #1부터 46미만의 임의의 값 생성합니다.
#더 쉽게 randint 
print(randint(1,45)) #1부터 45이하의 임의값 생성 이게 더 편하긴해 왜냐면 코드에서 1~45까지인걸 알수있으니