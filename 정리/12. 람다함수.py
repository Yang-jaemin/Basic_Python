# 익명의 함수 = 람다 함수

def plus(x):
    return x+2

print(plus(1))

plus_two = lambda x: x+2
print(plus_two(2))


# 이럴때 유용
a = [1,2,3,4,5]

print(list(map(plus,a))) # a값이 plus 함수에 들어가서 list로 저장
print(list(map(lambda x: x+1, a))) # 같은 표현 
