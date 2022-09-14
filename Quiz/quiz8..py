# quiz) 주어진 코드를 활용해서 부동산 프로그램을 작성하세요
# 출력예시)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class house:
    # 매물 초기화
    def __init__(self,location,house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year  
    # 매물 정보 표시
    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)
        
houses = []      #리스트 생성
house1 = house("강남","아파트","매매","10억","2010년")
house2 = house("마포","오피스텔","전세","5억","2007년")
house3 = house("송파","빌라","월세","500/50","2010년")

houses.append(house1)
houses.append(house2)
houses.append(house3)  #리스트에 추가

print("총 {0}대의 매물이 있습니다.".format(len(houses))) #리스트안에 객체 몇개인지 알기위해
for house in houses:
    house.show_detail()


