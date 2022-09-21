msg = "It is time"
x = "A"
tmp = 65

msg.upper() # 대문자화
msg.lower() # 소문자화

ord(x) # 아스키넘버 출력
chr(tmp) # 숫자에 맞는 아스키코드 출력

msg.isupper() # 대문자라면 true 아니면 false
msg.islower() # 소문자라면 true
msg.isalpha() # 알파벳일때만 true

msg.find('t') # msg에서 t를 찾아라 : 인덱스로 알려준다
print(msg.find('t')) # 1

msg.count('t') # t가 몇개인가
print(msg.count('t')) # 2

#슬라이싱

msg[:2] # index 0부터 2전까지
msg[3:5] # index 3부터 5전까지

len(msg) #길이를 알려준다 공백포함



#문자열 접근

for i in range(len(msg)): # 10 입력되어서 0~9까지 출력
    print(msg[i], end = ' ')
    
print()
    
for x in msg:
    print(x,end = ' ')
print()
    
# 대문자만 출력    
for x in msg:
    if x.isupper():
        print(x,end = ' ')
print()      


# 소문자만 출력
for x in msg:
    if x.islower():
        print(x,end = ' ')
print()    


# 알파벳으로 이루어져있는지
for x in msg:
    if x.isalpha():
        print(x,end = ' ')
print()        


# 아스키 코드

tmp = 'AZ'
for x in tmp:
    print(ord(x))
    
# 숫자를 아스키로 

tmp = 65
print(chr(tmp))