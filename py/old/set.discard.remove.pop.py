# n = int(input())
# s = set(map(int, input().split()))
# c = int(input())
# for _ in range(c):
#     getit = input().split()
#     store = True if len(list(getit)) > 1 else False
#     if store == False:
#         if getit[0] == 'pop':
#             exec('s.pop()')
#     else:
#         if getit[0] == 'remove':
#             exec('s.remove('+getit[1]+')')
#         elif getit[0] == 'discard':
#             exec('s.discard('+getit[1]+')')
# if list(s) == []:
#     print(0)
# else:
#     for i in list(s):
#         print(i,end=" ")

n = int(input())
s = set(map(int, input().split())) 
for _ in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))


