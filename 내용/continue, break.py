#반복문 continue, break

absent = [2,5]
nobook = [7]
for student in range(1,11): #[12345678910]
    if student in absent:
        continue # 밑의 문장을 실행하지않고 다음 문장을 합니다.
    elif student in nobook:
        print("오늘 수업 여기까지, {0}".format(student))
        break       #반복문 종료
    print("{0}, 책읽어".format(student))


        