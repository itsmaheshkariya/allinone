def printsorted(a, n, val, tempstore): 
    ans = []
    b =[[0 for x in range(2)] for y in range(n)] 
    for i in range(0, n):  
        b[i][0] = abs(a[i]-val)  
        b[i][1] = i 
    b.sort()  
    for i in range(0, tempstore):  
        ans.append(a[b[i][1]])
    return ans
darr = []
tempstore = []
store = []
for i in range(int(input())*2):
    count = 0
    tempstore = store
    store = list(map(int,input().split(' ')))
    if i % 2 != 0:
        save = printsorted(store, len(store), len(store), int(tempstore[1]))
        print(sum([(max(save) - x) for x in save]))
    darr.append(store)



# 3
# 4 3
# 3 1 9 100
# 6 2
# 5 5 1 2 3 4
# 5 5
# 7 7 1 7 7


# Case #1: 14
# Case #2: 0
# Case #3: 6