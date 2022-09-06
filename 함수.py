def account(): #함수 정의
    print("계좌가 개설되었습니다.")
    
account()

# 전달값 반환값

def deposit(balance,money):
    print("입금완료 잔액{0}".format(balance+money))
    return balance+money

def withdraw(balance, money): #출금
    if balance >= money:
        print("{0}원이 출금 되었습니다. 잔액은 {1}원 입니다.".format(money,balance - money))
        return balance - money
    else:
        print("출금 할 수 없습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance
balance = 0
balance = deposit(balance, 1000)
print(balance)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

def withdraw_night(balance, money): # 밤에 출금
    commission = 100
    if balance >= money+commission:
        print("{0}원이 출금 되었습니다. 잔액은 {1}원 입니다. 수수료는 {2}원 입니다.".format(money,balance - (money+commission),commission))
        balance = balance - (money+commission)
        return commission, balance
    else:
        print("출금 할 수 없습니다. 잔액은 {0}원 입니다.".format(balance))
        return commission, balance
    
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원 잔액은 {1}원입니다.".format(commission,balance)) 





# 기본값 설정하는 방법

#def profile(name,age,main_lang):
 #   print("이름 : {0}\t 나이 {1}\t 주 사용 언어: {2}" .format(name,age,main_lang))
    

#profile("양재민",23,"python")
#profile("최정욱",23,"java")

def profile(name,age = 23,main_lang = "python"): # 이렇게 옆에 입력을 함수에서 해주면 일일히 안적을 수 이씀
    print("이름 : {0}\t 나이 {1}\t 주 사용 언어: {2}" .format(name,age,main_lang))
    
profile("양재민")




# 키워드값 이용한 함수
def profile1(name,age,main_lang):
    print(name,age,main_lang)
    
profile1(name = "유재석",age = 29,main_lang = "python")
profile1(main_lang = "python",name = "유재석",age = 29)  #이런식으로 순서가 뒤 바뀌어있어도 가능합니다.