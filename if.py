weather = "비"

if weather == "비" or weather == "눈" :            # if 변수 == true :
 print("우산 챙겨라")
elif weather == "미세먼지":     # elif
     print("마스크 챙기라")
     
else:                         #위 조건 아니면 else 
    print("준비물 필요 없어요.")
    
    
    
food = input("오늘 뭐 먹어? ")

if food == "햄버거" or food == "피자":
    print("살빼라")
elif food == "샐러드" or food == "안먹어":
    print("배고프겠다.")
else: 
    print("그건 좀")
    
    
temp = int(input("기온은 어때요? ")) #숫자로 비교를 해야하니까 int형으로 자료형 변환 ㄱ

if temp > 30:
    print("덥다")
    
elif temp <= 30 and temp >=10 :
    print("좋네")
elif 0<= temp < 10 : #and 안써도 합쳐줄 수 있다
    print("춥다")