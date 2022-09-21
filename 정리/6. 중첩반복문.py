#중첩 반복문(2중 for문)

for i in range(5):
    print('i:',i, sep = '', end = ' ') # sep = ''을 해서 딱 붙게 나오고  end = ' '를 이용해서 옆으로 출력
    for j in range(5):
        print('j:',j,sep = '', end = ' ')
    print( )    
    
for i in range(5):
    for j in range(5):
        print("*",end = ' ')
    print() #별 5x5
    

for i in range(5):
    for j in range(i+1):
        print("*",end = ' ')
    print() 

# *
# **
# ***
# ****
# *****
    
    

for i in range(5):
    for j in range(5-i):
        print("*",end = ' ')
    print()

# *****
# ****
# ***
# **
# *
    
