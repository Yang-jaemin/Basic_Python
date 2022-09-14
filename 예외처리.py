#print("나누기 전용 계산기")
#num1 = int(input("첫번째 숫자를 입력하세요"))
#num2 = int(input("두번째 숫자를 입력하세요"))

#print("{0}/{1} = {2}".format(num1,num2,int(num1/num2))) #문자느면 종료 
try:    
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
