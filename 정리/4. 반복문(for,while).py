# range(10)
#   - 0부터 9까지 정수리스트를 만들어준다. (0부터 10개)

# range(1,11) 
#     - 1부터 11전까지 정수 리스트 만들어준다. 


# #for 문

# for i in range(10):
#     print(i) (0~9)

# for i in range(1,11)  
#     print(i) (1~10)

# for i in range(10, 0, -1) (10부터 0 전까지 -1 한다.)
#     print(i) (10~1)

# #while 문

# i = 1
# while i<= 10:
#     print(i)
#     i = i+1  (1~10 출력)



# # break, continue (for else 구문)
# i =1
# while True: 계속 반복
#     print(i)
#     if i == 10:
#         break
#     i+=1

# for i in range(1,11):
#     if i%2 == 0
#         continue (밑에 실행안하고 keep going)
#     print(i)
    
# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break
# else: 
#     print(11) (정상종료된다면 else 출력합니다.)