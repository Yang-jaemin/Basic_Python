# quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
#참석률을 높이기 위해 댓글 이벤트 합니다
#추첨을 통해 1명은 치킨 3명은 커피쿠폰 받습니다
#추첨 프로그램 작성하세요

#조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정합니다.
#조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건 3 : random 모듈의 shuffle 과 sample을 사용

#활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst) -> 12345
# shuffle(lst) -> 무작위 섞임
# print(sample(lst,1))

from random import *

lst = range(1,21) #1부터 21직전까지 숫자를 생성 range /range 타입
users = list(lst) #range -> list
shuffle(users)
winners = sample(users,4)

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))


#print("커피 당첨자: "+ lst[1:]  ) # list로