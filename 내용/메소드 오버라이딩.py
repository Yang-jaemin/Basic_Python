#메소드 오버라이딩
class unit:
    def __init__(self,name,hp,speed):  #__init__ : 생성자 self 빼고 3개 인자 동일해야 사용 가능
        self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. 속도 {2}".format(self.name,location,self.speed))
         
        
class attackunit(unit):
    def __init__(self,name,hp,speed,damage):
        #self.name = name                # 멤버 변수 : 어떤 클래스 내에서 정의되는 변수
        #self.hp = hp #상속 받을 거라 필요없음
        unit.__init__(self,name,hp,speed)
        self.damage = damage #unit에 데미지 없으니까 self. 으로 따로정의
    
    def attack(self,location):
        print("{0}: {1}방향으로 공격합니다. 데미지 :{2}".format(self.name,location,self.damage)) #self.변수 를통해서  클래스 안의 변수에 접근 self 없으며 전달값
        
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name,damage))
        self.hp -= damage
        print("{0} 현 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됨. ".format(self.name))
            
class fly:  #나는 기능
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 : {2}".format(name,location,self.flying_speed))
        
class fly_attack_unit(attackunit,fly):
    def __init__(self, name, hp, damage,flying_speed):
        attackunit.__init__(self,name,hp,0,damage) # 상속  // speed = 0인 이유는 날아가는 스피드가 따로 있으니까 #지상 speed는 0
        fly.__init__(self,flying_speed)  # 나는기능 상속
        
    def move(self,location):  #위에 unit에 move 함수가 있지만 새롭게 정의해서 공중유닛에서 사용할 수 있게 한다.
        print("[공중유닛 이동}")
        self.fly(self.name,location)
        
        
#발키리 : 공중유닛 ,14발 발사
valkyrie = fly_attack_unit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "5시")

# 벌쳐 : 지상 빠름  
vulture  = attackunit("벌쳐",80,10,20)

#배틀 크루져
battle_cruiser = fly_attack_unit("배틀크루져",500,25,3)
vulture.move("11시")
#battle_cruiser.fly("배틀크루저","9시")
battle_cruiser.move("9시")
