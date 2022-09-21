# 1) 1부터 n까지 홀수 출력
# 2) 1부터 n까지의 합 구하기daa
# 3) n의 약수 출력하기

#1)
n = int(input())
for i in range(1,n+1):
    if i%2 == 1:
        print(i)

#2)
sum = 0
for i in range(1,n+1):
    sum = sum+i
    
print(sum)
        
#3)
n = int(input())
for i in range(1,n+1):
    if n % i == 0:
        print(i,end = ' ') # 옆으로 출력