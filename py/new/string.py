a = list(input())
# a = input().split(' ')
print(set([(x,a.count(x)) for x in a ]))
# ma ma na ta
# ans ('ma',2) ('na',1) ('ta',1)