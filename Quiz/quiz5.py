# quiz5) 당신은 카카오택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있습니다 총 탑승 승객 수를 구하는 프로그램을 작성하세요

# 조건 1: 승객별 운행 소요 시간은 5~50분 사이의 난수 입니다.
# 조건 2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭 가능합니다.

# 출력문 예제)
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# ...
# 총 탑승 승객 2분
from random import *

count = 0

for sonnim in range(1,51): # 1~50
    time = int(random()*46)+5 #5부터 51미만의 난수    randrange(5,51) -> 5~51까지의 난수
    if 5 <= time <= 15:
        ride = "o"
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(ride,sonnim,time))
        count += 1
        
    else:
        ride = " "
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(ride,sonnim,time))
         
print("총 탑승 승객: {0}분".format(count))