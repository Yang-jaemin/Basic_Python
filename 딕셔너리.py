cabinet = {3:"유재석", 100:"김태호"}  #key 3은 유재석 key 100은 김태호
#print(cabinet[3])


#사전에서 값을 가져오는 방법 1번은 위

#print(cabinet[5]) 
# # 5라는 키가 없으니까 프로그램 오류 후 종료
print(cabinet.get(3))
print(cabinet.get(5,)) #get을 이용하면 none 이라고 출력하고 프로그램 계속진행 
print("hi")           # hi 출력

print(cabinet.get(5,"사용가능")) # none 대신에 다른 말을 얻고싶으면 

#사전 자료형 안에 어떤 값이 있는지 확인하는 작업
print(3 in cabinet) # True
print(5 in cabinet) # False


# 숫자가 아니여도 된다
cabinet2 = {"a-3":"유재석","a-100":"김태호"}
print(cabinet2["a-3"])
print(cabinet2["a-100"])

#새로운 값을 넣고 싶다
print(cabinet2)
cabinet2["c-20"] = "최정욱" #만약 C-20이 사용중이면 업데이트
cabinet2["a-3"] = "양재민"
print(cabinet2)

#지우고 싶다
del cabinet2["a-3"]
print(cabinet2)

#key들만 출력
print(cabinet2.keys())

#value들만 출력

print(cabinet2.values())

#key valu 쌍으로 출력하기
print(cabinet2.items())

#모든값을 지우기
cabinet2.clear()
print(cabinet2)
