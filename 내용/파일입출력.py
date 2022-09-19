#파일 생성 쓰기
score_file =open("score.txt","w",encoding="utf8") 
 #  w는 writing 쓰기위한 파일이라는 거임 그리고 utf8은 한글쓰기위해서
print("수학 : 0",file = score_file)
print("영어 : 50",file = score_file)

score_file.close()       # txt file이 만들어진다.

#이어쓰기
score_file = open("score.txt", "a", encoding = "utf8") # append 이어쓰고 싶다
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")

score_file.close()

#읽기
score_file = open("score.txt","r",encoding= "utf8") #read
print(score_file.read())
score_file.close()

#각각 읽기

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end ="") #줄별로 읽기 한줄읽고 커서는 다음줄
print(score_file.readline(), end ="") #4번 할 수있는 이유는 우리가 4줄인지 아니까 근데 모를때는 밑의 내용으로
print(score_file.readline(), end ="")
print(score_file.readline(), end ="")
score_file.close()

#몇줄인지 모를때 한줄 씩 읽기
score_file = open("score.txt","r",encoding="utf8")
while True: 
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()    #반복문을 이용해서 할 수 있다.


# 마지막 방법
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")  #for문을 통해서 할수있음