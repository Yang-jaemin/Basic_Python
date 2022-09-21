
a = [0]*10 # 0으로 초기화된 10개 값들어있는 리스트
print(a)

a = [[0]*3 for _ in range(3)] # 3번 반복하면서 1차원 리스트를 3번 만든다. = 2차원 리스트
print(a) # 표로 해석해라

a[0][1] = 2
print(a)

# 표처럼 출력하기
for x in a:
    print(x)

# 표처럼 출력하기 값처럼 출력  
for x in a:
    for y in x:
        print(y, end = '')
    print()