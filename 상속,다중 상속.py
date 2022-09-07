#일반 유닛
class unit:
    def __init__(self,name,hp):  #__init__ : 생성자 self 빼고 3개 인자 동일해야 사용 가능
        self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        self.hp = hp
         
        
class attackunit(unit):
    def __init__(self,name,hp,damage):
        #self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        #self.hp = hp #상속 받을 거라 필요없음
        unit.__init__(self,name,hp)
        self.damage = damage #unit에 데미지 없으니까 self. 으로 따로정의
    
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

#-------------------------------
# 메딕 공격 x  (상속으로 class unit을 수정햇음)
# 드랍쉽 : 공중 수송

class fly:  #나는 기능
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 : {2}".format(name,location,self.flying_speed))
        
class fly_attack_unit(attackunit,fly):
    def __init__(self, name, hp, damage,flying_speed):
        attackunit.__init__(self,name,hp,damage) # 상속
        fly.__init__(self,flying_speed)          # 나는기능 상속
        
        
#발키리 : 공중유닛 ,14발 발사
valkyrie = fly_attack_unit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "5시")