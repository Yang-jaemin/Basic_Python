#quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하세요
# 예시) www.naver.com
# 규칙 1) www. 제외
# 규칙 2) 처음 만나는 점(.) 이후 부분은 제외 naver.com -> naver
# 규칙 3) 남은 글자 중 처음 세자리(nav) + 글자 갯수(5)+ 글자 내 e갯수(1) "!"로 구성

from tokenize import maybe


site = "www.google.com" # nacver

index1 = site.index(".")
index2 = site.index(".", index1+1)

print(f"{index1},{index2}") #.은 3하고 9에 있다고 찾는거임

name = site[(index1+1):index2]
print("사이트 이름:"+name ) #남은 글자

length = len(name) # 남은 글자 글자갯수

nameof3 = name[:3] #남은글자 첫세자리

Ecount = name.count("e") #글자 내 e 갯수

print(f"비밀번호는 {nameof3}{length}{Ecount}! 입니다.")

url = "http://youtube.com"
my_str = url.replace("http://","") 
print(f"{my_str}") # http://를 빈칸이랑 대치해서 없애버려 조건1
my_str = my_str[0:my_str.index(".")]
print(f"{my_str}")
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) 

print(f"{password}")
