#슬라이싱
a =[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a)) #값이 몇이야


#값에 접근하는 법
for i in range(len(a)):
    print(a[i], end = ' ')

for x in a:
    print(x, end = ' ')
    
for x in a:
    if x%2 == 1:
        print(x, end = ' ')
        
for x in enumerate(a):
    print(x)  # (1,12) (2,36) 튜플형태로 보여준다.  enumerate()

# 튜플

b = (1,2,3,4,5) # 소괄호
# 리스트는 값 변경 가능한데 튜플은 불가
# b[0] = 7 (x)

for x in enumerate(a):
    print(x[0],x[1])  # (1,12) (2,36) 튜플형태로 보여준다.  enumerate()


############ 이런식으로 많이 사용!!
for index, value in enumerate(a):
    print(index,value)
print()


#   all
 
if all(60>x for x in a): # 모든 x가 조건에 모두 참이여만 true를 리턴한다.
    print("yes")
else:
    print("no")
    
#   any

if any(15>x for x in a): # 모든 x가 조건에 하나만 참이여도 true를 리턴한다.
    print("yes")
else:
    print("no")
