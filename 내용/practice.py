from random import *
lst = range(1,21)
users = list(lst)
winners = sample(users,4)
print(winners[1:])