#print("대기번호 : 1")
#print("대기번호 : 2")
#print("대기번호 : 3")
#print("대기번호 : 4")

#for waiting_no in [0,1,2,3,4]:
#   print("대기번호 : {0}".format(waiting_no))
    
    # [0,1,2,3,4] 처럼 순차적으로 커질때는 range를 사용할 수 있다.
    #randrange()
for waiting_no in range(5): #0에서 5직전
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(1,6): #1에서 5직전
    print("대기번호 : {0}".format(waiting_no))
    
    
starbucks = ["q","w","e"]

for customer in starbucks:
    print("{0}님 음료가 준비 되었습니다.".format(customer)) # in 뒤에 customer에 starbuck 인자들이 하나씩 들어가는거임
    





# 한줄 for

# 출석번호 1234, 앞에 100을 붙이기로했음 101 102 103 ...

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # student에서 하나씩 i로 불러와서 100을 더해주고 다시 students에 넣어주는거임 
print(students)

# 학생이름을 길이로 변환
students = ["Iron man","tor","i am groot"]
students = [len(i) for i in students]
print(students)

#  학생이름을 대문자로
students = ["Iron man","tor","i am groot"]
students = [i.upper() for i in students]
print(students)