# if __name__ == '__main__':
#     k,a = input(),list(map(int,input().split()))
#     av = len(a) // int(k)
#     # print(av)
#     a.sort()
#     for i in a:
#         if a.count(i) == 1:
#             print(i)
#             break
#         else:
#             for w in range(int(k)):
#                 a.remove(i)

k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))

        
    
# Sample Input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
# Sample Output
# 8