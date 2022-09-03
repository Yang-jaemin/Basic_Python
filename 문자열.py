#문자열 출력

sentence = "나는 소년입니다."
print(sentence)
sentence2 = '나는 소년입니다.'
print(sentence2)
sentence3 = '''
나는 소년이고 ,
파이썬은 쉬워          
''' #문장도 """ 과 '''로 다출력 가능
print(sentence3)






#   슬라이싱

jaemin= "990120-1234567"

print("성별 : "+ jaemin[7]) # 01234567 번째 숫자
print("연 : "+ jaemin[0:2]) # 0에서 2직전까지
print("월 : "+ jaemin[2:4]) # 2에서 4까지
print("일 : "+ jaemin[4:6]) #4에서 6까지
print("생년월일 : "+ jaemin[0:6]) #0에서 6직전까지
print("생년월일 : "+ jaemin[:6]) #처음에서 6직전까지
print("뒤 7자리 : "+ jaemin[7:]) #7에서 끝까지
print("뒤 7자리(뒤부터) : "+jaemin[-7:-1])#-7부터 -1직전까지 123456
print("뒤 7자리(뒤부터) : "+jaemin[-7:])#-7부터 끝까지







#문자열 처리함수

python = "Python is Amazing"
print(python.lower()) #소문자로 다 바꿔줌
print(python.upper()) #대문자로 다 바꿔줌
print(python[0].isupper()) #첫번째 값이 대문자인가요?
print(len(python)) # 파이썬 전체문자열길이
print(python.replace("Python","java")) #replace(a,b) a를 b로 바꿔준다

index = python.index("n") #n이 파이썬에서 어디에있냐
print(index)  # 5
index = python.index("n",index+1) #앞에 찾은거보다 1개부터 다시 n찾아서 위치저장
print(index)

print(python.find("java")) # 없으면 -1 출력(find)

#print(python.index("java"))# 없으면 프로그램 종료(find)

print(python.index("Python")) #출력값 0 아마 0부터 있다는 말인듯

print(python.count("n")) #n이 몇번나오나 세주느거







#문자열 포맷

print("a"+"b") # ab
print("a","b") # a b

    #방법 1 
print("나는 %d살입니다." %20) # %d 정수
print("나는 %s를 좋아해요" %"파이썬") # string 문자열 넣을때 %s
print("Apple은 %c로 시작해요." %"A") # %c c는 한글자만 받는거
    # %s는 사실 다쓸수 있어요
print("%s색과 %s색을 좋아해여" %("blue","red"))

    #방법2
print("나는 {}살입니다." .format(20)) # format()하고 {}으로도 삽입가능 앞에 . 붙이는거 잊지말ㄱㅣ
print("나는 {}색과 {}색을 좋아해요" .format("파란","빨간")) # 이것도 마찬가지
print("나는 {0}색과 {1}색을 좋아해요" .format("파란","빨간")) #순서지정도 가능

   #방법3
print("{age}살이며, {color}색을 좋아해요".format(age=20,color= "red")) #안에 변수선언해도 가능
print("{age}살이며, {color}색을 좋아해요".format(color= "red", age=20)) #바꿔도 가능

   #방법4
age = 20
color = "빨간"
print(f"{age}살이며, {color}색을 좋아해요") #이런 식으로 변수 선언한거 가져올 수 있음








# 탈출문자

print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견 \n백견이 불여일타") #\n 줄바꿈

print("저는 양재민입니다.")
print("저는 \"양재민\"입니다")  #\를 이용해서 따옴표를 살릴수있다.

# \\ : 문장내에서 \
print("양재민 ㅋㅋ\\") #\자체를 출력하려면 \\두번

#\r : 커서를 맨 앞으로 이동

print("Red Apple\rPine") # 맨앞으로 보내서 red()을 pine 으로 채움 햇갈리네 pineapple 출력

#\b
print("Redd\bapple") #backspace 앞에 한글자 지워줌 redapple

#\t : 탭
print("red\tapple") #red         apple 띄어줌




