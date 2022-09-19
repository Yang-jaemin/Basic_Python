#  while
#  5번 불렀는데 안나오면 커피 버리는 정책 사용
customer  = "토르"
index = 5 # 5번 부를거임

#while 조건 :

while index >= 1:
    print("{0}, 커피 준비되었습니다. {1}번 남았어요".format(customer,index))
    index -= 1 # index = index -1
    if index == 0:
        print("커피를 처분하겠습니다.")
        

customer = "양재민"
index = 1

#while True:
#   print("{0}님, 커피가 준비 되었습니다. 호출{1}회".format(customer,index)) #무한루프
#    index += 1     
    
sonnim = "양재민"
person = "unknown"

while person != sonnim:
    print("{0}님 커피 준비 됐습니다.".format(sonnim))
    person = input("이름이 어떻게 되세요? ")