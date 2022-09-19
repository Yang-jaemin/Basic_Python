gun = 10

def checkpoint(sodiers): #경계근무
    # gun = 20 # 2. 지역변수 초기화 해줘야해
    global gun # 3. global을 사용하면 밖의 전역변수 사용가능
    gun = gun - sodiers #남는 총 계산 -> 1. 지역변수여서 사용 불가
    print("[함수 내 남은 총] : {0}".format(gun))
    
print("전체 총: {0}".format(gun))

checkpoint(2)

print("전체 총: {0}".format(gun))


def checkpoint1(gun,sodiers):
    gun = gun - sodiers
    print("[함수 내 남은 총] : {0}".format(gun))
    return gun #지역 변수지만 gun을 리턴해주면 된다.

print("전체 총: {0}".format(gun))

gun = checkpoint1(gun,2) #전역변수 gun=10이 들어감 그리고 리턴도 전역변수 gun으로

print("전체 총: {0}".format(gun))