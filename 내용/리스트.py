# 리스트 []

#지하철 칸별로 10명,20명,30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway =["양재민","양지은","양유현"]
print(subway)

#활용 양재민이 어디칸에 있나? index

print(subway.index("양재민"))

# 여기서 박윤숙씨가 다음칸에 탐 append

subway.append("박윤숙") #append 맨뒤에 붙음
print(subway)

# 최정욱을 양재민 양지은 사이에 태우자 insert
subway.insert(1,"최정욱") # 배열도 0 ,1,2 똑같음
print(subway)

#지하철에 있는 사람 한명씩 꺼내기 pop
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명일까
subway.append("양재민")
print(subway) #양재민 추가

print(subway.count("양재민")) # 양 최 양 2번






#정렬도 가능해요  sort 순서대로 정렬해줍니다.

num_list =[5,2,3,4,1]
num_list.sort()
print(num_list)

#반대 순서로 정렬 reverse 반대의 순서로 정렬해줍니다.

num_list.reverse()
print(num_list)

# 모두 지우기 clear 리스트 안의 내용을 지웁니다.

num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용할 수 있습니다.
#mix_list = ["양재민",4,True]
#print(mix_list)

#배열끼리 합칠 수도 있다.  리스트 확장 extend
num_list =[5,4,3,2,1]
mix_list = ["양재민",4,True]

num_list.extend(mix_list)
print(num_list)
