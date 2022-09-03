print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))
#문자형
print("풍선")
print("z"*9)
#참 거짓
print(5<10)
print(5>10)
print(True)
print(not True)
print(not False)
#변수
#애완동물 소개해줘라
name = "연탄"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3 #true false로 나온다잉
#변수선언 중간에 선언가능 선언이후에는 마지막 선언 적용

print("우리집에는 연탄이라는 강아지가 있음 4살임 산책좋아함 근데 어른일까? True")
print("우리집 강아지는 연탄이")
print("연탄이는 4살")
print("연탄이는 어른일까?")
print("false") #줄바꿈을 안해줘도 코드 안에서 줄을 바꿔준다면 출력이 바꿔서나온다.


print("우리집에는" + name + "이라는" +animal+ "가 있음" + str(age) +"살임 "+ hobby +"좋아함 근데 어른일까?" +str(is_adult))
#+를 사용할때 정수형과 bool형은 str을 써줘라/
print("우리집에는",name, "이라는" ,animal, "가 있음",age, "살임 ",hobby,"좋아함 근데 어른일까?",is_adult)
#,를 사용하면 정수형과 bool형은 str을 안써줘도됨 근데 출력할때 한칸띄어서 나옴 ex)4살 -> 4 살
print("우리집 강아지는 연탄이")
print("연탄이는 4살")
print("연탄이는 어른일까?")
