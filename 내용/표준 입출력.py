#표준 입출력
print("python" + "java") #pythonjava
print("python","java") #python java

print("python","java",sep = ",") #python,java
print("python","java","js",sep = " vs ") #python vs java vs js 

#sep로 가운데에 넣을 수 있어

print("python","java",sep = ",",end ="?") # end : 문장의 끝부분을 물음표로 바꿔줘
print(" 무엇이 더 재미있을까요?") # 두 문장이 붙어서 나온다. 

import sys
print("python","java",file = sys.stdout) #표준출력
print("python","java",file = sys.stderr) #표준에러"

#출력 포멧 : 정렬

scores = {"수학":0 , "영어":50 ,"코딩": 100} #딕셔너리 키 밸류
for subject, score in scores.items(): #items key value 쌍으로
    #print(subject,score) #그냥 출력
    print(subject.ljust(8),str(score).rjust(4),sep =":") #ljust(8) 8칸의 여유두고 왼정렬 rjust(4) 4칸의 여유를 두고 오정렬
    
#은행 대기 순번 001 002 003 ..

for num in range(1,21):
    print(type(num)) #int 형이니까 str해줘라
    print("대기번호 : "+ str(num).zfill(3)) # 3개의 공간 확보하고 남는건 0으로 채워라 zfill(3) // range로 숫자받고 출력하려면 str
    
    
    
#표준 입력

answer = input("아무 값이나 입력하세요 : ") # str로 받음
print(answer)
    