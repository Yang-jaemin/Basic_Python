# 함수 만들기

# def add(a,b):
#     c = a+b
#     print(c)

# def add(a,b):
#     c = a+b
#     return c # 함수 종료된다.
    
def add(a,b):
    c = a+b
    d = a-b
    return c,d # 두개를 리턴할 수있음


def isprime(x):
    for i in range(2,x): #소수인지 판단할수있는 함수
        if x%i == 0:
            return False
    return True
        
print(add(3,2)) # return 값을 받아서 출력 / 반환값이 2개이상이면 튜플로 반환 (1,2) 이렇게



a = [12,13,7,9,19]
for x in a:
    if isprime(x):
        print(x, end = ' ')



