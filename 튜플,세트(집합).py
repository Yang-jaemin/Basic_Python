#리스트와 다르게 내용 변경 추가 힘들어요
#그치만 리스트보다 빨라요

menu = ("돈까스","치즈까스") #()
print(menu[0])
print(menu[1])

#값 추가 변경 불가

name = "양재민"
age = 23
hobby = "work out"
print(name,age,hobby) 

(name, age, hobby) = ("최정욱",24,"군대") #한번에 넣어줄수있음 튜플형태로
print(name,age,hobby)


#집합(set)
#중복 안되고 순서가 없음
set1 = {1,2,3,3,3} # {1,2,3} 출력

#교집합

java = {"양재민","최정욱","박형태"}
python = set(["양재민","박형태"]) #리스트를 세트 형태로
print(java & python) #자바와 파이똔의 교집합
print(java.intersection(python)) #이것도 교집합

#합집합

print(java | python)
print(java.union(python)) #합쳐져서 나온다잉

#차집합 (자바 가능 파이똔 불가능)

print(java -python)
print(java.difference(python)) #차집합

#파이썬 가능한 사람이 늘어남
python.add("최정욱")
print(python)

#java를 까먹었음

java.remove("양재민")
print(java)