class unit:
    def __init__(self,name,hp,damage):  #__init__ : 생성자 self 빼고 3개 인자 동일해야 사용 가능
        self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage)) 
        
class attackunit:
    def __init__(self,name,hp,damage):
        self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        self.hp = hp
        self.damage = damage
    
    def attack(self,location):
        print("{0}: {1}방향으로 공격합니다. 데미지 :{2}".format(self.name,location,self.damage)) #self.변수 를통해서  클래스 안의 변수에 접근 self 없으며 전달값
        
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name,damage))
        self.hp -= damage
        print("{0} 현 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됨. ".format(self.name))
            
# 파이어뱃 

firebat1 = attackunit("파이어뱃",50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
