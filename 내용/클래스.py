# 마린: 공격유닛 , 총쏨
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성 되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# 탱크 : 시즈 일반

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성 되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))
    
attack(name,"1시",damage)
attack(tank_name,"12시",tank_damage)
attack(tank2_name,"13시",tank2_damage)

# 이거를 클래스로

class unit:
    def __init__(self,name,hp,damage):  #__init__ : 생성자 self 빼고 3개 인자 동일해야 사용 가능
        self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage)) 
        
marine1 = unit("마린",40,5) #객체 , unit의 인스턴스
marine2 = unit("마린",40,5)
tank = unit("탱크", 150, 35)

# 레이스 : 공중유닛 , 비행기, 스텔스

raith = unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(raith.name,raith.damage))

# 다크아칸이 마컨으로 레이스 뺏음

raith2 = unit("뺏긴 레이스",80,5)
raith2.clocking = True #객체에 외부에서 추가로 변수를 만들수 있다. 객체.변수 이렇게

if raith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(raith2.name))