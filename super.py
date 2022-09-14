class unit:
    def __init__(self):
        print("unit 생성자")
        
class flyable:
    def __init__(self):
        print("flyable 생성자")
        
class fly_unit(unit,flyable):
    def __init__(self):
        #super().__init__() # 다중 상속시 주의: unit밖에 상속이 안됐음 , 앞에꺼만 됐음
        unit.__init__(self)
        flyable.__init__(self) # 다중 상속시에는 요렇게
        
        
        
#드랍쉽
dropship = fly_unit()  